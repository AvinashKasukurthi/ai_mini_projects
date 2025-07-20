# Mini Projects - LLM's and AI Agent Course

A collection of mini projects exploring AI integration using Ollama, focusing on practical applications of local language models.

## 📋 Overview

A collection of mini projects exploring AI integration using Ollama and frontier AI models, focusing on practical applications from basic API integration to advanced multi-model conversations.

## 🚀 Projects

1. **[Ollama Using Requests](./day_1_ollama_using_requests/README.md)** - Direct API integration with Ollama using HTTP requests (`python day_1_ollama_using_requests/ollama_requests.py`)
2. **[Ollama Website Summarizer](./day_2_ollama_website_summarizer/README.md)** - Web scraping and AI-powered content summarization (`python day_2_ollama_website_summarizer/ollama_webiste_summarizer.py`)
3. **[AI Brochure Generator](./day_3_brochure_using_ai/README.md)** - Multi-page web scraping and intelligent brochure generation (`python day_3_brochure_using_ai/brochure_ai.py`)
4. **[Frontier Models APIs](./day_4_frontier_models_apis/README.md)** - Multi-provider AI API integration and response comparison (`python day_4_frontier_models_apis/frontier_model_apis.py`)
5. **[Adversarial Conversation](./day_5_adversarial_conversation/README.md)** - Entertaining AI dialogue between contrasting GPT and Claude personalities (`python day_5_adversarial_conversation/adversarial_conversation.py`)

## 🛠️ Prerequisites

- Python 3.13+
- [Ollama](https://ollama.ai/) installed and running locally
- LLaMA 3.2 model pulled in Ollama

### Install Ollama and Model

```bash
# Install Ollama (macOS)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the LLaMA 3.2 model
ollama pull llama3.2

# Start Ollama server (if not running as service)
ollama serve
```

## 📦 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mini_projects
```

2. Install dependencies using uv (recommended) or pip:
```bash
# Using uv
uv sync

# Or using pip
pip install -r requirements.txt
```

## 🔧 Dependencies

- **ollama** (>=0.5.1) - Official Ollama Python client
- **requests** (>=2.32.4) - HTTP library for API calls
- **beautifulsoup4** (>=0.0.2) - HTML parsing for web scraping
- **rich** (>=14.0.0) - Terminal styling and markdown rendering
- **python-dotenv** (>=0.9.9) - Environment variable management
- **openai** (>=1.0.0) - OpenAI API client for GPT models
- **anthropic** (>=0.8.1) - Anthropic API client for Claude models

## 🏃‍♂️ Quick Start

1. Ensure Ollama is running:
```bash
ollama serve
```

2. Test the basic Ollama integration:
```bash
python day_1_ollama_using_requests/ollama_requests.py
```

3. Try the website summarizer:
```bash
python day_2_ollama_website_summarizer/ollama_webiste_summarizer.py
```

4. Generate an AI brochure:
```bash
python day_3_brochure_using_ai/brochure_ai.py
```

5. Compare frontier AI models:
```bash
python day_4_frontier_models_apis/frontier_model_apis.py
```

6. Watch adversarial AI conversation:
```bash
python day_5_adversarial_conversation/adversarial_conversation.py
```

## 🔧 Configuration

### Model Configuration
Both projects use the `llama3.2` model by default. You can modify the `MODEL` variable in each script to use different models:

```python
MODEL = "llama3.2"  # Change to your preferred model
```

### Ollama API Endpoint
The default Ollama API endpoint is `http://localhost:11434`. Modify the `OLLAMA_API` variable if your setup differs:

```python
OLLAMA_API = "http://localhost:11434/api/chat/"
```

## 📁 Project Structure

```
mini_projects/
├── README.md
├── LICENSE
├── pyproject.toml
├── main.py
├── day_1_ollama_using_requests/
│   ├── README.md
│   └── ollama_requests.py
├── day_2_ollama_website_summarizer/
│   ├── README.md
│   └── ollama_webiste_summarizer.py
├── day_3_brochure_using_ai/
│   ├── README.md
│   └── brochure_ai.py
├── day_4_frontier_models_apis/
│   ├── README.md
│   └── frontier_model_apis.py
└── day_5_adversarial_conversation/
    ├── README.md
    └── adversarial_conversation.py
```

## 🎯 Use Cases

- **Learning AI Integration**: Understand different approaches to AI model integration
- **Web Content Analysis**: Automatically summarize web articles and pages
- **API Development**: Learn HTTP-based AI API interactions
- **Content Processing**: Extract and process web content for AI analysis
- **Business Intelligence**: Generate professional brochures and company analysis
- **Marketing Automation**: Create compelling content for sales and recruitment

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Avinash Kasukurthi** - AI Agent Course Mini Projects

---

*Part of the AI Agent Course - exploring practical applications of local language models.*