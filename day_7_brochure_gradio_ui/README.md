# Day 7 - Brochure Gradio UI: AI-Powered Company Brochure Generator

A web-based interface for generating professional company brochures by analyzing website content using AI models with intelligent link discovery and streaming markdown output.

## 📋 Overview

This project combines the intelligent brochure generation capabilities from Day 3 with the user-friendly Gradio web interface from Day 6. It creates an interactive web application that generates professional company brochures by scraping and analyzing multiple pages from a company's website using AI.

## ✨ Features

- **Intelligent Web Scraping**: Automatically discovers and analyzes relevant company pages
- **AI-Powered Link Discovery**: Uses AI to identify important pages (About, Careers, etc.)
- **Multi-Model Support**: Choose between GPT-4o-mini and Claude-3-Haiku
- **Streaming Brochure Generation**: Real-time markdown brochure creation
- **Professional Output**: Structured brochures for customers, investors, and recruits
- **Web Interface**: Easy-to-use Gradio interface with form inputs
- **Content Filtering**: Removes irrelevant elements (scripts, styles, images)

## 🚀 How It Works

1. **Website Analysis**: Scrapes the main company landing page
2. **Link Discovery**: AI identifies relevant internal links (About, Careers, etc.)
3. **Content Extraction**: Gathers content from discovered pages
4. **Brochure Generation**: AI creates a professional markdown brochure
5. **Streaming Output**: Real-time display of the generated brochure

## 🔧 Prerequisites

- Python 3.13+
- API Keys for:
  - OpenAI (GPT models)
  - Anthropic (Claude models)

## 📦 Installation

1. **Install Dependencies**:
```bash
pip install gradio openai anthropic python-dotenv requests beautifulsoup4
```

2. **Set up Environment Variables**:
Create a `.env` file in the project directory:
```bash
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## 🏃‍♂️ Usage

```bash
python day_7_brochure_gradio_ui/brochure_gradio_ui.py
```

The web interface will launch at `http://localhost:7860` with the following inputs:
- **Company Name**: Enter the company name
- **Company URL**: Enter the company website URL
- **Model Selection**: Choose between GPT or Claude

## 🎯 Interface Components

### Input Fields
- **Company Name** (1 line): Name of the company for brochure generation
- **Company URL** (1 line): Main website URL to analyze
- **Model Selector**: Dropdown with GPT and Claude options

### Output
- **Response** (8 lines): Streaming markdown brochure output

## 🔍 AI-Powered Features

### Link Discovery System
```python
link_system_prompt = "You are provided with a list of links found on a webpage. \
You are able to decide which of the links would be most relevant to include in a brochure about the company, \
such as links to an About page, or a Company page, or Careers/Jobs pages."
```

### Intelligent Page Selection
The AI automatically identifies and prioritizes:
- About/Company pages
- Careers/Jobs pages
- Product/Services pages
- Mission/Values pages

### Content Processing
- **HTML Cleaning**: Removes scripts, styles, images, and input elements
- **Text Extraction**: Converts HTML to clean, readable text
- **Content Truncation**: Limits content to 5,000 characters for optimal processing

## 🏗️ System Architecture

### Website Class
```python
class Website:
    def __init__(self, url):
        # Fetches and processes website content
    def get_contents(self):
        # Returns formatted title and text content
```

### Link Discovery Functions
- `get_links_openai()`: Uses GPT for link analysis
- `get_links_claude()`: Uses Claude for link analysis
- Returns JSON with relevant links and their types

### Content Aggregation
- `get_all_details_openai()`: Aggregates content using GPT
- `get_all_details_claude()`: Aggregates content using Claude

### Streaming Generation
- `stream_brochure_openai()`: Streams GPT-generated brochures
- `stream_brochure_claude()`: Streams Claude-generated brochures

## 📊 Example Workflow

1. **Input**: Company Name: "TechCorp", URL: "https://techcorp.com"
2. **Analysis**: Discovers About, Careers, and Products pages
3. **Content Extraction**: Gathers text from all relevant pages
4. **AI Processing**: Generates professional brochure with:
   - Company overview
   - Products/services
   - Company culture
   - Career opportunities
   - Customer information

## 🔧 Configuration

### Model Settings
```python
# GPT Configuration
model="gpt-4o-mini"
response_format={"type": "json_object"}  # For link discovery

# Claude Configuration
model="claude-3-haiku-20240307"
temperature=0.7
max_tokens=1000
```

### System Prompts
```python
system_prompt = "You are an assistant that analyzes the contents of several relevant pages from a company website \
and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown.\
Include details of company culture, customers and careers/jobs if you have the information."
```

## 🎨 Brochure Structure

Generated brochures typically include:
- **Company Overview**: Mission, vision, and core business
- **Products & Services**: Key offerings and solutions
- **Company Culture**: Values, team, and work environment
- **Career Opportunities**: Job openings and growth paths
- **Customer Base**: Target markets and success stories
- **Contact Information**: How to get in touch

## 🔒 Security & Limitations

### Security Features
- **Environment Variables**: Secure API key management
- **User-Agent Headers**: Proper web scraping etiquette
- **Error Handling**: Graceful handling of failed page loads

### Content Limitations
- **Character Limit**: Content truncated to 5,000 characters
- **Page Restrictions**: Excludes Terms of Service, Privacy pages
- **Error Recovery**: Continues processing if individual pages fail

## 🚀 Advanced Features

### Intelligent Content Filtering
```python
for irrelevant in soup.body(["script", "style", "img", "input"]):
    irrelevant.decompose()
```

### JSON-Structured Link Discovery
```python
{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page", "url": "https://another.full.url/careers"}
    ]
}
```

### Streaming Response Handling
- **Real-time Updates**: Content appears as it's generated
- **Progressive Loading**: Users see immediate feedback
- **Smooth Experience**: No waiting for complete generation

## 🎓 Learning Outcomes

- **Web Scraping with AI**: Combine scraping with intelligent content analysis
- **Multi-Step AI Workflows**: Chain AI operations for complex tasks
- **Gradio Web Development**: Build interactive AI applications
- **Content Processing**: Clean and structure web content for AI analysis
- **Streaming Interfaces**: Implement real-time response displays

## 🤝 Use Cases

- **Sales Teams**: Generate company brochures for prospects
- **HR Departments**: Create recruitment materials
- **Marketing**: Produce company overview documents
- **Business Development**: Prepare investor presentations
- **Competitive Analysis**: Analyze competitor company structures

## 🔧 Customization

### Adding New Models
```python
def stream_model(company_name, url, model):
    if model == "NewModel":
        result = stream_brochure_new_model(company_name, url)
    # ... existing code
```

### Custom Brochure Sections
Modify the system prompt to include specific sections:
```python
system_prompt += "Include sections on: Technology Stack, Partnerships, Awards, and Financial Information."
```

### Enhanced Link Discovery
Customize link types to discover:
```python
"such as links to Technology pages, Partnership pages, Press Release pages"
```

## 🐛 Troubleshooting

### Common Issues
1. **Website Access Errors**: Some sites block automated requests
2. **Content Extraction**: Complex websites may not parse correctly
3. **API Rate Limits**: Manage multiple API calls efficiently
4. **Character Limits**: Large websites may exceed processing limits

### Debug Tips
- **Test with Simple Sites**: Start with basic company websites
- **Check API Keys**: Ensure all environment variables are set
- **Monitor Network**: Watch for failed HTTP requests
- **Content Validation**: Verify extracted text quality

## 📈 Performance Optimization

- **Concurrent Processing**: Could be enhanced with async/await
- **Caching**: Store processed content to avoid re-scraping
- **Content Prioritization**: Focus on most important pages first
- **Error Recovery**: Robust handling of partial failures

## 📄 License

Part of the AI Agent Course Mini Projects - MIT License
