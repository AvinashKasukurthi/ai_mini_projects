# Day 4: Frontier Models APIs

A comprehensive demonstration of integrating and comparing responses from leading AI frontier models including OpenAI's GPT models, Anthropic's Claude, and Google's Gemini.

## 📋 Overview

This project showcases how to interact with multiple state-of-the-art AI models through their respective APIs, allowing you to compare responses and capabilities across different providers. The script demonstrates API integration with:

- **OpenAI**: GPT-3.5 Turbo, GPT-4o Mini, and GPT-4o
- **Anthropic**: Claude 3.7 Sonnet
- **Google**: Gemini 2.5 Flash

## 🎯 Features

- **Multi-Provider Integration**: Seamless API calls to OpenAI, Anthropic, and Google AI
- **Response Comparison**: Side-by-side comparison of responses from different models
- **Environment Management**: Secure API key handling using environment variables
- **Rich Terminal Output**: Clean, formatted output for easy comparison
- **Error Handling**: API key validation and availability checking

## 🚀 Quick Start

1. **Set up your environment variables** by creating a `.env` file:
```bash
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

2. **Install dependencies** (if not already installed):
```bash
pip install openai anthropic google-genai python-dotenv rich
```

3. **Run the script**:
```bash
python frontier_model_apis.py
```

## 🔧 API Models Used

### OpenAI Models
- **GPT-3.5 Turbo**: Fast, cost-effective model for most tasks
- **GPT-4o Mini**: Lightweight version of GPT-4o with excellent performance
- **GPT-4o**: Latest flagship model with advanced reasoning capabilities

### Anthropic Models  
- **Claude 3.7 Sonnet**: Advanced reasoning model with strong analytical capabilities

### Google AI Models
- **Gemini 2.5 Flash**: Fast, efficient model optimized for quick responses

## 📝 Example Usage

The script demonstrates a simple joke-telling task across all models:

```python
system_message = "You are an assistant that is great at telling jokes"
user_prompt = "Tell a light-hearted joke for an audience of Data Scientists"
```

Each model responds with its own interpretation, allowing you to compare:
- Response style and tone
- Humor approach
- Technical understanding
- Output quality

## 🔑 API Key Setup

### OpenAI
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account and navigate to API keys
3. Generate a new API key
4. Add to your `.env` file as `OPENAI_API_KEY`

### Anthropic
1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Create an account and get your API key
3. Add to your `.env` file as `ANTHROPIC_API_KEY`

### Google AI
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create a project and generate an API key
3. Add to your `.env` file as `GOOGLE_API_KEY`

## 🛠️ Dependencies

```python
from openai import OpenAI              # OpenAI GPT models
import anthropic                       # Anthropic Claude models  
from google import genai               # Google Gemini models
from google.genai import types         # Google AI configuration types
import os                             # Environment variables
from dotenv import load_dotenv         # .env file loading
from rich.console import Console       # Rich terminal output
from rich.markdown import Markdown     # Markdown rendering
from rich.live import Live             # Live updates
```

## 📊 Model Comparison

| Model | Provider | Strengths | Use Cases |
|-------|----------|-----------|-----------|
| GPT-3.5 Turbo | OpenAI | Fast, cost-effective | General tasks, chatbots |
| GPT-4o Mini | OpenAI | Balanced performance/cost | Most applications |
| GPT-4o | OpenAI | Advanced reasoning | Complex analysis, research |
| Claude 3.7 Sonnet | Anthropic | Strong analytical skills | Research, writing |
| Gemini 2.5 Flash | Google | Fast responses | Real-time applications |

## 🔧 Configuration

### Temperature Setting
All models use `temperature=0.7` for balanced creativity and consistency. Adjust this value:
- `0.0-0.3`: More focused, deterministic responses
- `0.4-0.7`: Balanced creativity and consistency  
- `0.8-1.0`: More creative, diverse responses

### Max Tokens
Claude has a `max_tokens=200` limit set. Adjust based on your needs:
```python
claude_response = claude.messages.create(
    model="claude-3-7-sonnet-latest",
    system=system_message,
    messages=[{"role": "user", "content": user_prompt}],
    temperature=0.7,
    max_tokens=200,  # Adjust as needed
)
```

## 🎯 Use Cases

- **Model Evaluation**: Compare performance across different AI providers
- **Response Quality Analysis**: Evaluate output quality for specific tasks
- **Cost Optimization**: Test different models to find the best cost/performance ratio
- **API Learning**: Understand different API patterns and implementations
- **Research & Development**: Prototype applications using multiple AI providers

## 🔍 Example Output

```
OpenAI Key exists
Anthropic key exists  
Google Key exists

---- GPT 3.5 Turbo ----
[GPT-3.5 response]

---- GPT 4o Mini ----
[GPT-4o Mini response]

---- GPT 4o ----
[GPT-4o response]

---- Claude Sonnet 3.7 ----
[Claude response]

---- Google Gemini 2.5 Flash ----
[Gemini response]
```

## 🤝 Contributing

Feel free to expand this project by:
- Adding more AI providers (e.g., Cohere, Hugging Face)
- Implementing streaming responses
- Adding response evaluation metrics
- Creating automated comparison reports

## 📄 License

This project is part of the AI Agent Course Mini Projects and follows the same MIT License.

---

*Exploring the capabilities of frontier AI models through practical API integration.*
