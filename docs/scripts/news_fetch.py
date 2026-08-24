"""Daily fetch for techievenki.ai/news. No LLM, no API key — pure RSS/Atom,
dedup, and recency ranking. Runs in GitHub Actions on a schedule; writes
docs/_data/tech_news.yml, which the Jekyll page (docs/pages/news.html) renders.

Run locally to test:
    pip install feedparser pyyaml
    python docs/scripts/news_fetch.py

To verify a feed URL before adding it to news_config.yaml (corporate blogs
drift or 403 non-browser agents far more often than you'd expect):

    python -c "
    import feedparser
    d = feedparser.parse('<url>', agent='Mozilla/5.0')
    print(d.get('status'), len(d.entries), d.bozo)
    "

status=200, entries>0, bozo=False means it's good. bozo=True with entries=0
usually means the URL served HTML instead of a feed — wrong path, not a
network problem.
"""

from __future__ import annotations

import html
import re
import socket
import sys
from datetime import datetime, timedelta, timezone
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

import feedparser
import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "scripts" / "news_config.yaml"
OUTPUT_PATH = ROOT / "_data" / "tech_news.yml"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0 Safari/537.36"
)
FETCH_TIMEOUT = 15

TRACKING_PREFIXES = ("utm_", "mc_", "mkt_")
TRACKING_KEYS = {"ref", "source", "fbclid", "gclid", "igshid"}
_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")

# Overlap coefficient, gated by a minimum shared-token count — catches near-
# verbatim reposts across sources without merging two unrelated stories that
# happen to share a couple of common words. Same approach as Viveka's dedupe.
SIMILARITY_THRESHOLD = 0.70
MIN_SHARED_TOKENS = 3
STOPWORDS = {
    "a", "an", "the", "is", "are", "to", "for", "of", "and", "or", "in", "on",
    "with", "new", "now", "how", "why", "what", "introducing", "announcing",
    "launches", "launch", "released", "release", "update", "updates", "show", "hn",
}
_NON_WORD = re.compile(r"[^a-z0-9]+")


def canonicalize(url: str) -> str:
    p = urlparse(url.strip())
    netloc = p.netloc.lower()
    if netloc.startswith("www."):
        netloc = netloc[4:]
    query = [
        (k, v) for k, v in parse_qsl(p.query, keep_blank_values=False)
        if not k.lower().startswith(TRACKING_PREFIXES) and k.lower() not in TRACKING_KEYS
    ]
    path = p.path.rstrip("/") or "/"
    m = re.match(r"^/(abs|pdf)/(\d{4}\.\d{4,5})", path)
    if m and "arxiv.org" in netloc:
        path = f"/abs/{m.group(2)}"
    return urlunparse(("https", netloc, path, "", urlencode(sorted(query)), ""))


def clean_text(raw: str | None, limit: int = 400) -> str:
    if not raw:
        return ""
    text = _WS.sub(" ", html.unescape(_TAG.sub(" ", raw))).strip()
    return text[:limit]


def normalise(title: str) -> str:
    words = [w for w in _NON_WORD.sub(" ", title.lower()).split() if w not in STOPWORDS]
    return " ".join(sorted(set(words)))


def similar(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    ta, tb = set(a.split()), set(b.split())
    shared = ta & tb
    ratio = SequenceMatcher(None, a, b).ratio()
    if len(shared) >= MIN_SHARED_TOKENS:
        return max(ratio, len(shared) / min(len(ta), len(tb)))
    return ratio


def _published(entry) -> datetime | None:
    for key in ("published_parsed", "updated_parsed"):
        parsed = entry.get(key)
        if parsed:
            return datetime(*parsed[:6], tzinfo=timezone.utc)
    return None


def fetch_tile(tile: dict, window_hours: int, verbose: bool = False) -> list[dict]:
    """Fetch every feed in a tile, return raw items inside the time window."""
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=window_hours)
    socket.setdefaulttimeout(FETCH_TIMEOUT)

    items: list[dict] = []
    for feed in tile["feeds"]:
        try:
            parsed = feedparser.parse(feed["url"], agent=USER_AGENT)
        except Exception as exc:
            print(f"    ! {feed['name']}: {exc}")
            continue

        status = parsed.get("status")
        if status and status >= 400:
            print(f"    ! {feed['name']}: HTTP {status}")
            continue
        if parsed.bozo and not parsed.entries:
            reason = parsed.get("bozo_exception", "unreadable feed")
            print(f"    ! {feed['name']}: {reason}")
            continue

        kept = 0
        for entry in parsed.entries:
            link = entry.get("link")
            title = clean_text(entry.get("title"), 300)
            if not link or not title:
                continue
            pub = _published(entry)
            if pub and pub < cutoff:
                continue
            items.append({
                "title": title,
                "url": link,
                "canonical_url": canonicalize(link),
                "summary": clean_text(entry.get("summary") or entry.get("description"), 240),
                "source": feed["name"],
                "weight": feed.get("weight", 2),
                "published_at": pub.isoformat() if pub else None,
                "_sort_time": pub or now,  # undated items sort as "now" — freshest, not lost
            })
            kept += 1
        if verbose:
            print(f"    · {feed['name']}: {kept} in window ({len(parsed.entries)} total)")
    return items


def dedupe(items: list[dict], window_hours: int = 48) -> list[dict]:
    """Collapse near-duplicate coverage. Keeps the lowest-weight (most
    authoritative) copy of each story; records how many reposts it absorbed.

    Only ever merges items from DIFFERENT sources. Two consecutive releases
    from the same changelog feed ("v2.1.240", "v2.1.241") are textually
    near-identical but are not reposts of each other — without this guard
    the similarity check collapses a whole release history into one entry.
    """
    window = timedelta(hours=window_hours)
    enriched = [dict(it, _norm=normalise(it["title"])) for it in items]
    enriched.sort(key=lambda i: i["_sort_time"])

    clusters: list[list[dict]] = []
    for item in enriched:
        for group in clusters:
            if any(
                m["source"] != item["source"]
                and abs((item["_sort_time"] - m["_sort_time"]).total_seconds()) <= window.total_seconds()
                and similar(item["_norm"], m["_norm"]) >= SIMILARITY_THRESHOLD
                for m in group
            ):
                group.append(item)
                break
        else:
            clusters.append([item])

    out = []
    for group in clusters:
        primary = min(group, key=lambda i: (i["weight"], -i["_sort_time"].timestamp()))
        primary["dupe_count"] = len(group) - 1
        primary.pop("_norm", None)
        out.append(primary)
    return out


def rank(items: list[dict], limit: int) -> list[dict]:
    """Freshest first; weight breaks ties so a primary source edges out an
    aggregator that happened to post at the same moment."""
    items.sort(key=lambda i: (-i["_sort_time"].timestamp(), i["weight"]))
    return items[:limit]


def build(verbose: bool = False) -> dict:
    config = yaml.safe_load(CONFIG_PATH.read_text())
    window_hours = config.get("window_hours", 72)
    per_tile = config.get("items_per_tile", 8)

    tiles_out = []
    for tile in config["tiles"]:
        print(f"  {tile['id']}")
        raw = fetch_tile(tile, window_hours, verbose=verbose)
        deduped = dedupe(raw)
        top = rank(deduped, per_tile)
        for it in top:
            it.pop("_sort_time", None)
            it.pop("canonical_url", None)
        tiles_out.append({
            "id": tile["id"],
            "title": tile["title"],
            "items": top,
        })
        print(f"    -> {len(raw)} fetched, {len(deduped)} after dedup, {len(top)} shown")

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "tiles": tiles_out,
    }


def main() -> None:
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    print("fetching tiles")
    data = build(verbose=verbose)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        yaml.dump(data, sort_keys=False, allow_unicode=True, width=100)
    )
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
