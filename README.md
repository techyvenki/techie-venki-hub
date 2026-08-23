# techie-venki-hub

Techie Venki Hub site sources.

## Local testing (Jekyll)

Use these steps to run and validate the docs site locally before pushing.

### 1) Install Ruby + tooling (one-time)

```bash
brew install ruby
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
gem install jekyll bundler
```

### 2) Prepare dependencies in this repo

From the repository root:

```bash
cd /Users/techyvenki/Documents/techievenkisite/techievenkihub/techie-venki-hub
```

If `Gemfile` does not exist, create it:

```bash
cat > Gemfile <<'EOF'
source "https://rubygems.org"

gem "jekyll"
gem "webrick"
gem "jekyll-remote-theme"
gem "jekyll-seo-tag"
gem "jemoji"
EOF
```

Install gems:

```bash
bundle install
```

### 3) Run the docs site locally

```bash
bundle exec jekyll serve --source docs --livereload
```

Open:

```text
http://127.0.0.1:4000
```

### 4) Validate before push

```bash
bundle exec jekyll build --source docs
git status --short
git diff --stat
```

### 5) Optional clean rebuild

```bash
bundle exec jekyll clean --source docs
bundle exec jekyll build --source docs
```
