# Mini Projects - AI Agent Course

A collection of mini projects exploring AI integration using Ollama, focusing on practical applications of local language models.

## 📋 Overview

This repository contains several mini projects that demonstrate different approaches to working with AI models:

1. **Ollama Using Requests** - Direct API integration with Ollama using HTTP requests
2. **Ollama Website Summarizer** - Web scraping and content summarization using Ollama

## 🚀 Projects

### 1. Ollama Using Requests (`ollama_using_requests/`)

A simple demonstration of how to interact with Ollama's API using raw HTTP requests.

**Features:**
- Direct API calls to Ollama using the `requests` library
- Non-streaming chat completion
- Uses LLaMA 3.2 model for business AI applications

**Usage:**
```bash
python ollama_using_requests/ollama_requests.py
```

### 2. Ollama Website Summarizer (`ollama_website_summarizer/`)

An intelligent website content summarizer that scrapes web pages and provides concise summaries using AI.

**Features:**
- Web scraping with BeautifulSoup
- Content cleaning (removes scripts, styles, images, inputs)
- AI-powered summarization using Ollama
- Markdown-formatted output
- Handles news and announcements

**Usage:**
```bash
python ollama_website_summarizer/ollama_webiste_summarizer.py
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

## 🏃‍♂️ Quick Start

1. Ensure Ollama is running:
```bash
ollama serve
```

2. Test the basic Ollama integration:
```bash
python ollama_using_requests/ollama_requests.py
```

3. Try the website summarizer:
```bash
python ollama_website_summarizer/ollama_webiste_summarizer.py
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
├── ollama_using_requests/
│   └── ollama_requests.py
└── ollama_website_summarizer/
    └── ollama_webiste_summarizer.py
```

## 🎯 Use Cases

- **Learning AI Integration**: Understand different approaches to AI model integration
- **Web Content Analysis**: Automatically summarize web articles and pages
- **API Development**: Learn HTTP-based AI API interactions
- **Content Processing**: Extract and process web content for AI analysis

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Avinash Kasukurthi** - AI Agent Course Mini Projects

---

*Part of the AI Agent Course - exploring practical applications of local language models.*