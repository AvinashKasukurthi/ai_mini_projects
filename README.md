# Mini Projects - LLM's and AI Agent Course

A collection of mini projects exploring AI integration using Ollama, focusing on practical applications of local language models.

## 📋 Overview

This repository contains several mini projects that demonstrate different approaches to working with AI models:

1. **Ollama Using Requests** - Direct API integration with Ollama using HTTP requests
2. **Ollama Website Summarizer** - Web scraping and content summarization using Ollama
3. **AI Brochure Generator** - Multi-page web scraping and intelligent brochure generation
4. **Frontier Models APIs** - Integration and comparison of leading AI models (OpenAI, Anthropic, Google)

## 🚀 Projects

### 1. [Ollama Using Requests](./day_1_ollama_using_requests/README.md)

A simple demonstration of how to interact with Ollama's API using raw HTTP requests.

- **Location**: `day_1_ollama_using_requests/`
- **Focus**: Direct API integration using the `requests` library
- **Model**: LLaMA 3.2 for business AI applications

**Quick Start:**
```bash
python day_1_ollama_using_requests/ollama_requests.py
```

### 2. [Ollama Website Summarizer](./day_2_ollama_website_summarizer/README.md)

An intelligent website content summarizer that scrapes web pages and provides concise summaries using AI.

- **Location**: `day_2_ollama_website_summarizer/`
- **Focus**: Web scraping and AI-powered content summarization
- **Features**: BeautifulSoup parsing, content cleaning, markdown output

**Quick Start:**
```bash
python day_2_ollama_website_summarizer/ollama_webiste_summarizer.py
```

### 3. [AI Brochure Generator](./day_3_brochure_using_ai/README.md)

An intelligent brochure generator that creates professional company brochures by analyzing website content using AI and streaming markdown output.

- **Location**: `day_3_brochure_using_ai/`
- **Focus**: Multi-page web scraping, intelligent link analysis, and AI-powered brochure generation
- **Features**: Rich terminal output, streaming markdown, real-time generation

**Quick Start:**
```bash
python day_3_brochure_using_ai/brochure_ai.py
```

### 4. [Frontier Models APIs](./day_4_frontier_models_apis/README.md)

A comprehensive demonstration of integrating and comparing responses from leading AI frontier models including OpenAI's GPT models, Anthropic's Claude, and Google's Gemini.

- **Location**: `day_4_frontier_models_apis/`
- **Focus**: Multi-provider AI API integration and response comparison
- **Features**: OpenAI GPT models, Anthropic Claude, Google Gemini, API key management

**Quick Start:**
```bash
python day_4_frontier_models_apis/frontier_model_apis.py
```

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
└── day_4_frontier_models_apis/
    ├── README.md
    └── frontier_model_apis.py
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