# Ollama Website Summarizer

An intelligent website content summarizer that scrapes web pages and provides concise summaries using AI.

## 📋 Overview

This project combines web scraping capabilities with AI-powered summarization to automatically extract and summarize content from websites. It uses BeautifulSoup for HTML parsing and Ollama for generating intelligent summaries.

## ✨ Features

- **Web Scraping**: Automatically fetches website content using requests
- **Content Cleaning**: Removes irrelevant elements (scripts, styles, images, inputs)
- **AI-Powered Summarization**: Uses Ollama LLaMA 3.2 for intelligent content analysis
- **Markdown Output**: Formatted summaries in markdown
- **News Detection**: Special handling for news and announcements
- **Title Extraction**: Automatically extracts and includes page titles

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- [Ollama](https://ollama.ai/) installed and running locally
- LLaMA 3.2 model pulled in Ollama

### Dependencies

- `ollama` - Official Ollama Python client
- `beautifulsoup4` - HTML parsing library
- `requests` - HTTP library for web scraping

### Installation

1. Ensure Ollama is running:
```bash
ollama serve
```

2. Make sure you have the LLaMA 3.2 model:
```bash
ollama pull llama3.2
```

3. Run the script:
```bash
python ollama_webiste_summarizer.py
```

## 🔧 Configuration

### Model Configuration
```python
MODEL = "llama3.2"  # Change to your preferred model
```

### User Agent Headers
```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
```

## 📝 Code Structure

### Website Class
The `Website` class handles web scraping and content extraction:

```python
class Website:
    def __init__(self, url):
        # Fetches website content
        # Parses HTML with BeautifulSoup
        # Extracts title and clean text
```

**Key Features:**
- Automatic content fetching
- HTML parsing and cleaning
- Title extraction
- Text content extraction with proper formatting

### Content Processing Functions

1. **`get_user_prompt(website)`**: Constructs the AI prompt with website content
2. **`get_messages_for(website)`**: Creates the message structure for Ollama
3. **`summarize(url)`**: Main function that coordinates the summarization process
4. **`display(url)`**: Wrapper function for easy usage

## 🎯 Usage Examples

### Basic Usage
```python
# Summarize a website
display("https://example.com")
```

### Custom Implementation
```python
# Create a Website object
website = Website("https://example.com")

# Get the summary
summary = summarize("https://example.com")
print(summary)
```

### Batch Processing
```python
urls = [
    "https://example1.com",
    "https://example2.com",
    "https://example3.com"
]

for url in urls:
    print(f"\n--- Summary for {url} ---")
    display(url)
```

## 🧹 Content Cleaning

The scraper automatically removes:
- `<script>` tags and JavaScript code
- `<style>` tags and CSS styling
- `<img>` tags and images
- `<input>` tags and form elements

This ensures the AI focuses on meaningful textual content.

## 🤖 AI Prompting

### System Prompt
```python
SYSTEM_PROMPT = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."
```

### User Prompt Structure
- Website title inclusion
- Content summarization instructions
- Special handling for news and announcements
- Complete website text content

## 📊 Example Output

```markdown
# Website Summary: Example News Site

## Overview
This website provides the latest technology news and updates...

## Key Headlines
- New AI breakthrough announced
- Tech company releases innovative product
- Industry analysis and trends

## Recent Announcements
- Partnership announcement between companies
- New feature rollouts
- Upcoming events and conferences
```

## 🔧 Customization

### Change Target Website
```python
# Modify the last line of the script
display("https://your-target-website.com")
```

### Adjust AI Model
```python
MODEL = "llama3.1"  # or any other available model
```

### Modify System Prompt
```python
SYSTEM_PROMPT = "Your custom instructions for the AI assistant..."
```

### Custom Content Filtering
```python
# Add more elements to remove
for irrelevant in website_soup.body(["script", "style", "img", "input", "nav", "footer"]):
    irrelevant.decompose()
```

## 🚨 Troubleshooting

### Common Issues

1. **Connection Errors**: Check internet connectivity and website availability
2. **Parsing Errors**: Some websites may have unusual HTML structures
3. **Rate Limiting**: Some websites may block automated requests
4. **Large Content**: Very large websites may exceed AI context limits

### Error Handling Improvements

```python
try:
    website = Website(url)
    summary = summarize(url)
    print(summary)
except requests.RequestException as e:
    print(f"Error fetching website: {e}")
except Exception as e:
    print(f"Error during summarization: {e}")
```

## 🎯 Use Cases

- **Content Research**: Quickly summarize articles and blog posts
- **News Monitoring**: Automated news summarization
- **Competitive Analysis**: Summarize competitor websites
- **Documentation Review**: Extract key information from documentation sites
- **Academic Research**: Summarize research papers and academic websites

## 🔍 Technical Details

### Web Scraping Strategy
- Uses realistic User-Agent headers to avoid blocking
- Handles dynamic content through BeautifulSoup parsing
- Extracts text content while preserving structure

### AI Integration
- Uses Ollama's chat completion API
- Implements structured message format for better results
- Focuses on content summarization with markdown formatting

## 📚 Learning Resources

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library Guide](https://docs.python-requests.org/)
- [Ollama Python Client](https://github.com/ollama/ollama-python)
- [Web Scraping Best Practices](https://scrapehero.com/web-scraping-best-practices/)

---

*Part of the AI Agent Course Mini Projects*
