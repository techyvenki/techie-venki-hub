---
title: "Getting Started with Azure AI Services"
tags: [Azure AI Services, REST APIs, SDKs, Resource Deployment, Cloud Development]
style: fill
color: info
description: Complete guide to provisioning, configuring, and integrating Azure AI Services using REST APIs and SDKs. Learn setup, authentication, and best practices for cloud-based AI applications.
---

# Getting Started with Azure AI Services

<div style="background: linear-gradient(135deg, #0078D4 0%, #00BCF2 100%); color: white; padding: 1.5rem; border-radius: 10px; margin-bottom: 2rem;">
  <div style="display: flex; justify-content: space-between; align-items: center;">
    <div>
      <h2 style="margin: 0; color: white;">🚀 Practical Implementation Guide</h2>
      <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">From Resource Creation to API Integration</p>
    </div>
  </div>
</div>

## 📋 Table of Contents

<!--ts-->
   * [Learning Objectives](#-learning-objectives)
   * [Setting Up Azure AI Services](#setting-up-azure-ai-services)
   * [Choosing Your Resource Type](#choosing-your-resource-type)
   * [Deployment Considerations](#deployment-considerations)
   * [Understanding Endpoints and Keys](#understanding-endpoints-and-keys)
   * [Working with REST APIs](#working-with-rest-apis)
   * [Using Azure AI SDKs](#using-azure-ai-sdks)
   * [Quick Testing with Azure Portal](#quick-testing-with-azure-portal)
   * [Best Practices](#best-practices)
<!--te-->

---

## 🎯 Learning Objectives

By the end of this section, you will be able to:

<div style="background: #E3F2FD; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #1976D2; margin: 1rem 0;">

- ✅ **Understand the range of AI-powered services** available in Azure

- ✅ **Create and manage Azure AI resources** within your subscription with proper configuration

- ✅ **Work with REST APIs** to call Azure AI Services from your applications

- ✅ **Leverage Azure AI SDKs** (Python, .NET, Node.js) to simplify integration

- ✅ **Secure your AI services** using authentication keys and best practices

- ✅ **Setup and integrate AI services** into cloud-based applications

</div>

---

## 🏗️ Setting Up Azure AI Services

Creating your first Azure AI Service is straightforward. Follow these steps to deploy a resource in the Azure Portal.

### Step-by-Step Portal Setup

#### Step 1: Create Your Resource

Navigate to the **Azure Portal** and create a new resource:

<div style="background: #FFF3E0; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #F57C00; margin: 1rem 0;">

1. **Select Your Subscription** - Choose the Azure subscription where you want to deploy the service
2. **Assign to Resource Group** - Create a new resource group or select an existing one to organize related resources
3. **Choose Region** - Select a region close to your users for:
   - ⚡ **Lower Latency** - Faster response times
   - 📊 **Better Performance** - Optimal user experience
   - 📋 **Compliance** - Meet data residency requirements

</div>

#### Step 2: Configure Your Instance

<div style="background: #E3F2FD; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #1976D2; margin: 1rem 0;">

- **Resource Name**: Give your instance a descriptive name (e.g., `my-ai-language-service`)
- **Pricing Tier**: Choose your plan:
  - **Free Tier** - Perfect for experimentation and learning (limited requests)
  - **Standard S0** - Production workloads with higher quotas
  - **Other Tiers** - Specialized plans for specific use cases

</div>

#### Step 3: Review and Create

Review all settings and click **Create**. Azure will deploy your resource in a few moments.

---

## 🎯 Choosing Your Resource Type

Azure offers two approaches to organizing AI services. Choose based on your team's needs:

### 1️⃣ Multi-Service Resource

<div style="display: grid; grid-template-columns: 1fr; gap: 1rem; margin: 1rem 0;">

<div style="background: #E8F5E9; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #388E3C;">

#### 🎯 When to Use Multi-Service

**One resource, multiple capabilities:**
- Single API key and endpoint for all services
- Simplified billing and management
- Teams need access to various AI services

**Available Services:**
- 💬 Azure AI Language
- 👁️ Azure AI Vision
- 📄 Azure AI Document Intelligence
- 🎤 Azure AI Speech
- 🤖 Azure OpenAI

**How to Create:**
Create under **"Azure AI Services"** in the marketplace

**Best For:**
- 🏢 Enterprise teams using multiple AI services
- 🔄 Projects requiring cross-service capabilities
- 💰 Cost optimization with shared quotas

</div>

</div>

### 2️⃣ Single-Service Resource

<div style="display: grid; grid-template-columns: 1fr; gap: 1rem; margin: 1rem 0;">

<div style="background: #FCE4EC; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #C2185B;">

#### 🎯 When to Use Single-Service

**Dedicated resource for one service:**
- Unique API key and endpoint per service
- Granular control and isolation
- Clear separation of concerns

**Examples:**
- **Vision-only Team**: Create "Azure AI Vision" resource
- **Language-only Team**: Create "Azure AI Language" resource
- **Speech-only Team**: Create "Azure AI Speech" resource

**How to Create:**
Search for individual service name and create directly from marketplace

**Best For:**
- 👥 Teams focused on a single capability
- 🔐 Projects requiring strict access control
- 📊 Detailed cost tracking per service

</div>

</div>

### Comparison Table

| Factor | Multi-Service | Single-Service |
|--------|---------------|----------------|
| **Number of Services** | Multiple (Vision, Language, etc.) | One specific service |
| **API Keys** | Single shared key | Unique per service |
| **Endpoint** | One endpoint | One per service |
| **Management** | Simplified | More granular |
| **Billing** | Consolidated | Separated by service |
| **Best For** | Enterprise, broad teams | Specialized teams |
| **Access Control** | Team-level | Role-level per service |

---

## 📋 Deployment Considerations

Before deploying, plan these important factors:

### 1. Subscription and Region

<div style="background: #E0F7FA; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #00838F; margin: 1rem 0;">

**What to Consider:**

- **Azure Subscription**: Choose based on billing and organizational structure
- **Geographic Region**: Select a region based on:
  - 📍 **User Location** - Deploy near your users for lower latency
  - ⚖️ **Compliance Requirements** - Some data must stay in specific regions (GDPR, etc.)
  - 💵 **Cost** - Pricing varies by region
  - 🔄 **Service Availability** - Not all services available in all regions

**Example Regions:**
- `eastus` - East US (Virginia)
- `westeurope` - West Europe (Netherlands)
- `southeastasia` - Southeast Asia (Singapore)

</div>

### 2. Pricing and Tiers

<div style="background: #F3E5F5; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #7B1FA2; margin: 1rem 0;">

**Tier Options:**

| Tier | Cost | Use Case | Request Limits |
|------|------|----------|-----------------|
| **Free** | $0 | Learning, experimentation | Limited |
| **Standard S0** | Pay-per-use | Production | Higher quotas |
| **Premium** | Dedicated instances | High-scale workloads | Custom limits |

**💡 Tip:** Start with Free tier to explore, then upgrade to Standard for production applications.

</div>

### 3. Security and Access Control

<div style="background: #FFEBEE; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #F44336; margin: 1rem 0;">

**Control Access Using:**

- 🔑 **API Keys** - Basic authentication for development
- 🆔 **Azure Role-Based Access Control (RBAC)** - Manage who can access your service:
  - `Contributor` - Full access to manage resources
  - `Reader` - View resources only
  - `Cognitive Services User` - Call API endpoints only

**Best Practice:** Use Azure RBAC in production to grant minimum required permissions.

</div>

### Summary: Planning Ahead

<div style="background: #FFF8E1; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #FFC107; margin: 1rem 0;">

**These decisions affect three critical factors:**

1. **💰 Cost** - Region, tier, and multi-service vs single-service affect billing
2. **⚡ Performance** - Region selection impacts latency and response times
3. **🔐 Governance** - Security settings and access control ensure proper oversight

**Action Item:** Plan these choices before deploying to avoid costly changes later.

</div>

---

## 🔑 Understanding Endpoints and Keys

Once your resource is deployed, you receive three essential pieces of information:

### What You Get

#### 1. Endpoint (The Service URL)

<div style="background: #E3F2FD; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #1976D2; margin: 1rem 0;">

The **endpoint** is the URL your application uses to call Azure AI services:

```
https://ai102.cognitiveservices.azure.com/
```

**Service-Specific Endpoints:**

**OpenAI Services:**
```
Language APIs:  https://ai102.openai.azure.com/
DALL-E APIs:    https://ai102.openai.azure.com/
Whisper APIs:   https://ai102.openai.azure.com/
```

**Speech Services:**
```
Speech-to-Text (Standard):  https://eastus.stt.speech.microsoft.com/
Text-to-Speech (Neural):    https://eastus.tts.speech.microsoft.com/
Custom Voice:               https://ai102.cognitiveservices.azure.com/
```

**Other Services:**
```
Content Safety:              https://ai102.cognitiveservices.azure.com/
Computer Vision:             https://ai102.cognitiveservices.azure.com/
Content Understanding:       https://ai102.services.ai.azure.com/
```

</div>

#### 2. Authentication Keys (Secrets)

<div style="background: #E8F5E9; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #388E3C; margin: 1rem 0;">

Azure provides **two unique authentication keys** - either one can be used:

```
Key 1: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Key 2: yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
```

**Why Two Keys?**
- 🔄 **Key Rotation** - Regenerate one key while keeping the other active
- 🔐 **Security** - Compromise of one key doesn't require immediate service interruption

**⚠️ Important:** Store keys securely using Azure Key Vault, not in code!

</div>

#### 3. Location (Azure Datacenter)

<div style="background: #FFF3E0; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #F57C00; margin: 1rem 0;">

This specifies which Azure datacenter is hosting your service:

```
eastus (East US - Virginia)
```

This information is useful for compliance verification and understanding where your data is processed.

</div>

---

## 🔌 Working with REST APIs

REST APIs allow you to call Azure AI Services directly over HTTP.

### How REST APIs Work

<div style="background: #E3F2FD; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #1976D2; margin: 1rem 0;">

**The Flow:**

1. **Your Application** sends a JSON request containing text or an image URL
2. **Azure AI Service** processes the input using AI models
3. **Azure responds** with JSON results:
   - Sentiment analysis
   - Translation
   - Object detection
   - Or other AI capabilities

</div>

### REST API Request Structure

#### Example: Analyze Text Sentiment

```
POST https://ai102.cognitiveservices.azure.com/language/:analyze-text?api-version=2023-04-15-preview
```

#### Breaking Down the Request

##### 1. Authentication Header

<div style="background: #FFEBEE; padding: 1rem; border-radius: 8px; border-left: 4px solid #F44336; margin: 1rem 0;">

**API Key Authentication:**
```
Ocp-Apim-Subscription-Key: YOUR_API_KEY
```

**Alternative: Microsoft Entra ID (Azure AD)**
- Generate a bearer token from your user credentials or service principal
- Include in header: `Authorization: Bearer {token}`
- More secure for enterprise applications

</div>

##### 2. Request Body (JSON Format)

<div style="background: #E8F5E9; padding: 1rem; border-radius: 8px; border-left: 4px solid #388E3C; margin: 1rem 0;">

Send data in JSON format matching the service's expected schema:

```json
{
  "kind": "SentimentAnalysis",
  "analysisInput": {
    "documents": [
      {
        "id": "1",
        "language": "en",
        "text": "The product quality is excellent!"
      }
    ]
  },
  "parameters": {
    "modelVersion": "latest"
  }
}
```

**Key Points:**
- Follow the exact schema for your service
- Ensure data types match (strings, numbers, etc.)
- Include required fields like language and document ID

</div>

##### 3. Response Handling

<div style="background: #E0F7FA; padding: 1rem; border-radius: 8px; border-left: 4px solid #00838F; margin: 1rem 0;">

Azure returns structured JSON results:

```json
{
  "kind": "SentimentAnalysis",
  "results": {
    "documents": [
      {
        "id": "1",
        "sentiment": "positive",
        "scores": {
          "positive": 0.95,
          "neutral": 0.04,
          "negative": 0.01
        }
      }
    ]
  }
}
```

Parse these results to take action in your application.

</div>

---

## 🛠️ Using Azure AI SDKs

SDKs simplify working with Azure AI Services by handling authentication, requests, and responses automatically.

### Why Use SDKs?

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin: 1rem 0;">

<div style="background: #E3F2FD; padding: 1rem; border-radius: 8px; border-left: 4px solid #1976D2;">
  <strong>⚙️ SDK Functionality</strong><br>
  Runtime libraries that manage authentication, requests, and responses automatically
</div>

<div style="background: #E8F5E9; padding: 1rem; border-radius: 8px; border-left: 4px solid #388E3C;">
  <strong>⚡ Developer Benefits</strong><br>
  Faster integration, reduce boilerplate code, enhance efficiency
</div>

<div style="background: #FFF3E0; padding: 1rem; border-radius: 8px; border-left: 4px solid #F57C00;">
  <strong>📚 Multiple Languages</strong><br>
  Python, .NET (C#), Java, Node.js official support
</div>

</div>

### Supported SDKs

| Language | Package | Use Case |
|----------|---------|----------|
| **Python** | `azure-ai-textanalytics`, `azure-cognitiveservices-*` | Data science, scripting |
| **.NET** | `Azure.AI.TextAnalytics`, `Microsoft.Azure.CognitiveServices.*` | Enterprise applications |
| **Node.js** | `@azure/ai-text-analytics`, `@azure/cognitiveservices-*` | Web applications |
| **Java** | `com.azure:azure-ai-textanalytics` | Backend services |

### Python SDK Example

#### Installation

```bash
# Install core credentials
pip install azure-core

# Install service-specific SDK (example: Text Analytics)
pip install azure-ai-textanalytics
```

#### Code Example: Sentiment Analysis

```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Initialize client
endpoint = "https://ai102.cognitiveservices.azure.com/"
key = "YOUR_API_KEY"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Analyze sentiment
documents = ["The product is amazing!"]
result = client.analyze_sentiment(documents, language="en")

# Process results
for doc in result:
    print(f"Sentiment: {doc.sentiment}")
    print(f"Scores: {doc.confidence_scores}")
```

#### Key Components

<div style="background: #E3F2FD; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #1976D2; margin: 1rem 0;">

- **`AzureKeyCredential`** - Handles authentication with your API key
- **`TextAnalyticsClient`** - The main client for calling the service
- **`analyze_sentiment()`** - Method to analyze text sentiment
- All request/response handling is abstracted away

</div>

### .NET SDK Example

```csharp
using Azure;
using Azure.AI.TextAnalytics;

// Initialize client
var endpoint = new Uri("https://ai102.cognitiveservices.azure.com/");
var credentials = new AzureKeyCredential("YOUR_API_KEY");
var client = new TextAnalyticsClient(endpoint, credentials);

// Analyze sentiment
string text = "The product quality is excellent!";
DocumentSentiment sentiment = client.AnalyzeSentiment(text);

Console.WriteLine($"Sentiment: {sentiment.Sentiment}");
```

### Benefits of Using SDKs

<div style="background: #F3E5F5; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #7B1FA2; margin: 1rem 0;">

✅ **Reduced Boilerplate** - No manual HTTP request formatting  
✅ **Error Handling** - Built-in retry logic and exception handling  
✅ **Type Safety** - IntelliSense and compile-time checks  
✅ **Maintenance** - Microsoft updates SDKs regularly  
✅ **Consistency** - Same API patterns across all services

</div>

---

## 🧪 Quick Testing with Azure Portal

Before writing code, test AI service capabilities directly in the Azure Portal using the **Quickstart blade**:

<div style="background: #E8F5E9; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #388E3C; margin: 1rem 0;">

### Steps to Test

1. **Open your resource** in the Azure Portal
2. **Click "Quickstart"** in the left navigation
3. **Select your preferred language** (Python, .NET, Node.js, etc.)
4. **Copy sample code** and run it immediately
5. **See results** without additional setup

### Why This Is Useful

- 🚀 **Quick Validation** - Verify your service is working
- 💡 **Learn by Example** - See real code patterns
- 🔑 **Auto-populated Credentials** - No need to copy keys manually
- 📝 **Language Specific** - Code matches your preferred language

</div>

---

## ✅ Best Practices

<div style="background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%); padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">

### Security

🔐 **Never hardcode API keys** - Use environment variables or Azure Key Vault  
🔐 **Rotate keys regularly** - Use one key while regenerating the other  
🔐 **Use Azure RBAC** - Grant minimum required permissions per user  
🔐 **Enable managed identity** - For Azure-to-Azure service communication

### Performance

⚡ **Choose the right region** - Deploy close to your users  
⚡ **Use connection pooling** - Reuse client instances  
⚡ **Implement caching** - Cache results for repeated queries  
⚡ **Monitor quotas** - Stay within rate limits

### Development

💻 **Start with Free tier** - Experiment before production costs  
💻 **Use Azure Portal Quickstart** - Test before coding  
💻 **Implement error handling** - Handle rate limits and timeouts  
💻 **Log API calls** - Track usage and troubleshoot issues

### Cost Optimization

💰 **Use multi-service resources** - If using multiple services  
💰 **Right-size pricing tiers** - Choose Standard only if needed  
💰 **Monitor usage** - Track API calls and adjust strategy  
💰 **Use Azure Cost Management** - Set budgets and alerts

</div>

---

## 📝 Summary

<div style="background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%); padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">

✅ **Create resources** using multi-service or single-service approach  
✅ **Plan deployment** considering region, pricing, and security  
✅ **Secure endpoints and keys** using best practices  
✅ **Choose between REST APIs** (direct HTTP) or **SDKs** (simplified libraries)  
✅ **Test capabilities** using Azure Portal Quickstart before coding  
✅ **Implement production applications** with proper error handling and monitoring

</div>

---

## 🔗 Next Steps

<div style="display: flex; justify-content: space-between; margin-top: 2rem;">
  <a href="introduction-to-ai-azure-services.html" style="padding: 1rem; background: #f5f5f5; border-radius: 8px; text-decoration: none; color: #333;">
    ← Introduction to AI
  </a>
  <a href="azure-ai-language-services.html" style="padding: 1rem; background: #0078D4; border-radius: 8px; text-decoration: none; color: white;">
    Next: Azure AI Language Services →
  </a>
</div>
