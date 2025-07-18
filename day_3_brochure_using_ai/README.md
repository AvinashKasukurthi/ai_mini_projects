# AI Brochure Generator

An intelligent brochure generator that creates professional company brochures by analyzing website content using AI and streaming markdown output.

## 📋 Overview

This project combines advanced web scraping, intelligent link analysis, and AI-powered content generation to automatically create comprehensive company brochures. It scrapes multiple pages from a company's website and generates a professional brochure suitable for customers, investors, and recruits.

## ✨ Features

- **Intelligent Web Scraping**: Multi-page content extraction with smart link filtering
- **AI-Powered Link Analysis**: Automatically identifies relevant pages (About, Careers, etc.)
- **Rich Terminal Output**: Beautiful streaming markdown display using Rich library
- **Real-time Generation**: Live streaming of brochure content as it's being generated
- **Comprehensive Content**: Includes company culture, customers, and career information
- **Error Handling**: Robust handling of failed page requests
- **Content Truncation**: Smart content limiting to stay within AI context limits

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- [Ollama](https://ollama.ai/) installed and running locally
- LLaMA 3.2 model pulled in Ollama

### Dependencies

- `ollama` - Official Ollama Python client
- `beautifulsoup4` - HTML parsing library
- `requests` - HTTP library for web scraping
- `rich` - Terminal styling and markdown rendering
- `python-dotenv` - Environment variable management

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
python brochure_ai.py
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

### Content Limits
```python
user_prompt = user_prompt[:5_000]  # Truncate if more than 5,000 characters
```

## 📝 Code Architecture

### Website Class
Enhanced website scraping with link extraction:

```python
class Website:
    def __init__(self, url):
        # Fetches website content
        # Parses HTML with BeautifulSoup
        # Extracts title, text, and links
        # Cleans irrelevant content
```

**Key Features:**
- URL storage for reference
- Content cleaning (scripts, styles, images, inputs)
- Link extraction and filtering
- Title and text content extraction

### Core Functions

1. **`get_links(url)`**: AI-powered relevant link identification
2. **`get_all_details(url)`**: Multi-page content aggregation
3. **`create_brochure(company_name, url)`**: Non-streaming brochure generation
4. **`stream_brochure(company_name, url)`**: Real-time streaming brochure creation

## 🎯 Usage Examples

### Basic Usage
```python
# Generate a brochure for a company
stream_brochure("Anthropic", "https://www.anthropic.com/")
```

### Non-streaming Version
```python
# Generate without streaming
brochure = create_brochure("Company Name", "https://company.com")
print(brochure)
```

### Custom Company Analysis
```python
# Analyze different companies
companies = [
    ("OpenAI", "https://openai.com"),
    ("Hugging Face", "https://huggingface.co"),
    ("Anthropic", "https://www.anthropic.com")
]

for name, url in companies:
    print(f"\n--- Generating brochure for {name} ---")
    stream_brochure(name, url)
```

## 🔍 Intelligent Link Analysis

The system uses AI to identify relevant pages for brochure content:

### Link System Prompt
```python
link_system_prompt = "You are provided with a list of links found on a webpage. \
You are able to decide which of the links would be most relevant to include in a brochure about the company, \
such as links to an About page, or a Company page, or Careers/Jobs pages."
```

### Filtered Link Types
- About pages
- Company information
- Careers/Jobs pages  
- Product pages
- Team/Leadership pages

### Excluded Content
- Terms of Service
- Privacy policies
- Email links
- Navigation elements

## 🎨 Rich Terminal Features

### Streaming Display
- **Live Updates**: Real-time markdown rendering
- **Refresh Rate**: 10 updates per second for smooth display
- **Accumulated Content**: Progressive content building
- **Completion Indicator**: Clear completion status

### Visual Elements
```python
console = Console()
with Live(console=console, refresh_per_second=10) as live:
    # Streaming content display
    markdown = Markdown(accumulated_content)
    live.update(markdown)
```

## 🤖 AI Prompting Strategy

### System Prompt
```python
system_prompt = "You are an assistant that analyzes the contents of several relevant pages from a company website \
and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown.\
Include details of company culture, customers and careers/jobs if you have the information."
```

### User Prompt Structure
1. **Company identification** with name
2. **Content aggregation** from multiple pages
3. **Markdown formatting** instructions
4. **Target audience** specification (customers, investors, recruits)

## 📊 Example Output

```markdown
# Anthropic - AI Safety Company

## About
Anthropic is an AI safety company focused on developing safe, beneficial AI systems...

## Mission & Values
- Safety-first approach to AI development
- Responsible AI research and deployment
- Constitutional AI methodology

## Products & Services
- Claude: Advanced AI assistant
- API services for developers
- Research publications

## Company Culture
- Research-driven environment
- Collaborative team structure
- Focus on long-term AI safety

## Careers
- Competitive benefits package
- Remote-friendly work environment
- Opportunities in AI research and safety
```

## 🔧 Customization

### Change Target Company
```python
# Modify the function call
stream_brochure("Your Company", "https://yourcompany.com")
```

### Adjust Content Limits
```python
# Increase context window
user_prompt = user_prompt[:10_000]  # Larger content limit
```

### Modify AI Model
```python
MODEL = "llama3.1"  # or any other available model
```

### Custom System Prompt
```python
system_prompt = "Your custom instructions for brochure generation..."
```

### Additional Link Types
```python
# Add more link filtering in get_links_user_prompt
"Include links to Products, Services, Team pages as well."
```

## 🚨 Troubleshooting

### Common Issues

1. **Network Errors**: Some websites may block automated requests
2. **Link Resolution**: Relative links may not resolve correctly
3. **Content Limits**: Large websites may exceed context windows
4. **Rate Limiting**: Multiple requests may trigger rate limits

### Error Handling

The system includes robust error handling:
```python
try:
    result += f"\n\n{link['type']}\n{Website(link['url']).get_contents()}"
except Exception as e:
    print(f"Getting error on {link['type']}")
    continue
```

### Debugging Tips

1. **Check Ollama Status**: Ensure Ollama is running
2. **Verify URLs**: Test URLs manually for accessibility
3. **Monitor Output**: Watch for error messages during scraping
4. **Content Size**: Check if content exceeds limits

## 🎯 Use Cases

- **Sales & Marketing**: Generate professional company brochures
- **Investment Pitches**: Create investor-focused company summaries
- **Recruitment**: Develop attractive company profiles for candidates
- **Competitive Analysis**: Analyze competitor positioning and messaging
- **Content Strategy**: Understand how companies present themselves

## 🔍 Technical Details

### Multi-page Strategy
1. **Landing Page Analysis**: Extract main company information
2. **Link Identification**: AI-powered relevant page discovery
3. **Content Aggregation**: Combine information from multiple sources
4. **Intelligent Summarization**: Generate cohesive brochure content

### Streaming Implementation
- **Rich Library**: Advanced terminal formatting and display
- **Live Updates**: Real-time content rendering
- **Markdown Support**: Proper formatting with headers, lists, and emphasis
- **Progress Indication**: Clear start and completion markers

## 🚀 Advanced Features

### Batch Processing
```python
def generate_multiple_brochures(companies):
    for company_name, url in companies:
        print(f"\n{'='*60}")
        print(f"Generating brochure for: {company_name}")
        print(f"{'='*60}")
        stream_brochure(company_name, url)
```

### Export Functionality
```python
def save_brochure(company_name, url, filename=None):
    brochure = create_brochure(company_name, url)
    filename = filename or f"{company_name.lower().replace(' ', '_')}_brochure.md"
    with open(filename, 'w') as f:
        f.write(brochure)
    print(f"Brochure saved to {filename}")
```

## 📚 Learning Resources

- [Rich Library Documentation](https://rich.readthedocs.io/)
- [BeautifulSoup Guide](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Ollama Python Client](https://github.com/ollama/ollama-python)
- [Web Scraping Ethics](https://blog.apify.com/web-scraping-ethics/)
- [Markdown Syntax Guide](https://www.markdownguide.org/basic-syntax/)

---

*Part of the AI Agent Course Mini Projects*
