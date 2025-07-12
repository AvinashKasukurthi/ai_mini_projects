# Ollama Using Requests

A simple demonstration of how to interact with Ollama's API using raw HTTP requests.

## 📋 Overview

This project demonstrates direct integration with Ollama's API using the Python `requests` library. It showcases how to make HTTP POST requests to the Ollama chat endpoint without using the official Ollama Python client.

## ✨ Features

- **Direct API Integration**: Uses raw HTTP requests instead of SDK
- **Non-streaming Chat**: Implements synchronous chat completion
- **Business AI Focus**: Configured with prompts for business AI applications
- **Simple Implementation**: Minimal code for easy understanding
- **Error Handling**: Basic status code checking

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- [Ollama](https://ollama.ai/) installed and running locally
- LLaMA 3.2 model pulled in Ollama

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
python ollama_requests.py
```

## 🔧 Configuration

### API Endpoint
```python
OLLAMA_API = "http://localhost:11434/api/chat/"
```

### Model Configuration
```python
MODEL = "llama3.2"  # Change to your preferred model
```

### Headers
```python
HEADERS = {
    "Content-Type": "application/json",
}
```

## 📝 Code Structure

The script includes:

1. **API Configuration**: Sets up the Ollama API endpoint and headers
2. **Message Structure**: Defines the chat message format
3. **Payload Creation**: Constructs the JSON payload for the API request
4. **HTTP Request**: Makes a POST request to the Ollama API
5. **Response Handling**: Processes and displays the API response

## 🔍 Example Usage

The current implementation asks about AI applications in business:

```python
messages = [
    {
        "role": "user",
        "content": "Describe some of the best applications of AI in business.",
    },
]
```

## 📊 Expected Output

```
Status Code: 200
Response: [AI-generated response about business applications]
```

## 🎯 Use Cases

- **Learning API Integration**: Understand how to work with REST APIs
- **Custom Implementations**: Build custom clients without SDK dependencies
- **Debugging**: Direct control over HTTP requests for troubleshooting
- **Lightweight Applications**: Minimal dependencies for simple use cases

## 🔧 Customization

### Change the Model
```python
MODEL = "llama3.1"  # or any other available model
```

### Modify the Prompt
```python
messages = [
    {
        "role": "user",
        "content": "Your custom prompt here",
    },
]
```

### Enable Streaming
```python
payload = {
    "model": MODEL,
    "messages": messages,
    "stream": True,  # Enable streaming responses
}
```

## 🚨 Troubleshooting

### Common Issues

1. **Connection Refused**: Ensure Ollama is running (`ollama serve`)
2. **Model Not Found**: Pull the required model (`ollama pull llama3.2`)
3. **Port Issues**: Check if Ollama is running on the default port 11434

### Error Responses

The script checks for successful status codes (200) and displays the response content. For debugging, you can add:

```python
if response.status_code != 200:
    print("Error:", response.text)
```

## 📚 Learning Resources

- [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [Python Requests Documentation](https://docs.python-requests.org/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

*Part of the AI Agent Course Mini Projects*
