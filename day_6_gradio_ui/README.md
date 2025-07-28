# Day 6 - Gradio UI: Multi-Model AI Interface

A web-based interface for comparing responses from multiple AI models (GPT, Claude, and Gemini) using Gradio, featuring real-time streaming responses.

## 📋 Overview

This project creates an interactive web interface using Gradio that allows users to chat with different AI models and compare their responses. The interface supports streaming responses for a more interactive experience, similar to ChatGPT's interface.

## ✨ Features

- **Multi-Model Support**: Integrate with GPT-4o-mini, Claude-3-Haiku, and Gemini-2.5-Flash
- **Streaming Responses**: Real-time streaming output for better user experience
- **Model Selection**: Dropdown to choose between different AI models
- **Clean Web Interface**: Simple and intuitive Gradio-based UI
- **Environment Variable Management**: Secure API key handling with dotenv
- **Markdown Support**: AI responses formatted in markdown for better readability

## 🔧 Prerequisites

- Python 3.13+
- API Keys for:
  - OpenAI (GPT models)
  - Anthropic (Claude models)
  - Google AI (Gemini models)

## 📦 Installation

1. **Install Dependencies**:
```bash
pip install gradio openai anthropic google-generativeai python-dotenv beautifulsoup4 requests
```

2. **Set up Environment Variables**:
Create a `.env` file in the project directory:
```bash
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

## 🏃‍♂️ Usage

```bash
python day_6_gradio_ui/gradio_ui.py
```

The interface will launch in your default web browser at `http://localhost:7860`.

## 🎯 How It Works

1. **Model Initialization**: The app initializes connections to all three AI providers
2. **API Key Validation**: Checks and displays which API keys are properly configured
3. **Streaming Functions**: Individual streaming functions for each AI model:
   - `stream_gpt()`: Streams responses from OpenAI GPT-4o-mini
   - `stream_claude()`: Streams responses from Anthropic Claude-3-Haiku
   - `stream_gemini()`: Streams responses from Google Gemini-2.5-Flash
4. **Model Router**: `stream_model()` function routes requests to the appropriate model
5. **Web Interface**: Gradio interface with text input and model selection dropdown

## 🖥️ Interface Components

- **Message Input**: Multi-line text box for user prompts (6 lines)
- **Model Selector**: Dropdown with options for GPT, Claude, and Gemini
- **Response Output**: Large text area displaying streaming AI responses (8 lines)
- **No Flagging**: Flagging is disabled for cleaner interface

## 🔧 Configuration

### Model Settings
```python
# GPT Configuration
model="gpt-4o-mini"
system_message="You are a helpful assistant that responds in markdown"

# Claude Configuration
model="claude-3-haiku-20240307"
temperature=0.7
max_tokens=1000

# Gemini Configuration
model="gemini-2.5-flash"
```

### System Prompts
All models use the same system message:
```python
system_message = "You are a helpful assistant that responds in markdown"
```

## 🌐 Web Interface Features

- **Real-time Streaming**: See responses appear character by character
- **Model Comparison**: Easy switching between different AI models
- **Markdown Rendering**: Properly formatted responses with markdown support
- **Clean Design**: Minimal and focused interface design
- **Auto-launch**: Automatically opens in your default browser

## 📊 Example Usage

1. **Start the Application**:
   ```bash
   python day_6_gradio_ui/gradio_ui.py
   ```

2. **Select a Model**: Choose from GPT, Claude, or Gemini in the dropdown

3. **Enter Your Message**: Type your question or prompt in the text area

4. **Watch Streaming Response**: See the AI response appear in real-time

## 🔒 Security Features

- **Environment Variables**: API keys stored securely in `.env` file
- **Key Validation**: Checks API key presence and displays partial keys for verification
- **No Logging**: Flagging disabled to prevent data collection

## 🚀 Advanced Features

### Streaming Implementation
- **GPT**: Uses OpenAI's streaming API with delta content accumulation
- **Claude**: Uses Anthropic's streaming with text stream processing
- **Gemini**: Uses Google's streaming with chunk text aggregation

### Error Handling
- Graceful handling of missing API keys
- Model validation in the routing function
- Robust streaming with null content checking

## 🎓 Learning Outcomes

- **Gradio Framework**: Learn to build web interfaces for AI applications
- **Streaming APIs**: Understand real-time response streaming implementation
- **Multi-Model Integration**: Work with different AI provider APIs simultaneously
- **Web UI Design**: Create user-friendly interfaces for AI tools
- **API Management**: Handle multiple API keys and configurations

## 🤝 Use Cases

- **Model Comparison**: Compare responses from different AI models
- **Educational Tool**: Demonstrate AI capabilities to students or colleagues
- **Prototyping**: Quick interface for testing AI model performance
- **Research**: Study differences in AI model behavior and responses
- **Demo Applications**: Showcase AI integration capabilities

## 🔧 Customization

### Adding New Models
To add new AI models, create a new streaming function and update the router:

```python
def stream_new_model(prompt):
    # Your streaming implementation
    yield response

def stream_model(prompt, model):
    if model == "NewModel":
        result = stream_new_model(prompt)
    # ... existing code
```

### UI Modifications
Customize the Gradio interface by modifying the `gr.Interface()` configuration:

```python
view = gr.Interface(
    fn=stream_model,
    inputs=[
        gr.Textbox(label="Custom Label", lines=10),
        gr.Dropdown(choices, label="Custom Model Selector"),
    ],
    outputs=[gr.Textbox(label="Custom Output", lines=12)],
    title="Custom Title",
    description="Custom Description"
)
```

## 🐛 Troubleshooting

### Common Issues
1. **API Key Errors**: Ensure all API keys are properly set in `.env` file
2. **Port Conflicts**: Gradio uses port 7860 by default; change if needed
3. **Import Errors**: Install all required dependencies
4. **Streaming Issues**: Check internet connection and API rate limits

### Debug Mode
Enable debug output by adding print statements or using Gradio's built-in debugging:

```python
view.launch(debug=True)
```

## 📄 License

Part of the AI Agent Course Mini Projects - MIT License
