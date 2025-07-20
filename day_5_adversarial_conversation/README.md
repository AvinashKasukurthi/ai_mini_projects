# Day 5 - Adversarial Conversation

An entertaining demonstration of adversarial AI conversation between OpenAI's GPT and Anthropic's Claude models with opposite personalities.

## 🎭 Overview

This project creates a fascinating dialogue between two AI models with contrasting personalities:
- **GPT (Argumentative)**: Snarky, disagreeable, challenges everything
- **Claude (Polite)**: Courteous, agreeable, tries to find common ground and calm situations

## 🚀 Features

- **Dual AI Integration**: Uses both OpenAI GPT-4o-mini and Anthropic Claude-3-haiku
- **Personality Contrast**: Demonstrates how system prompts create vastly different conversational styles
- **Multi-turn Conversation**: Runs 5 rounds of back-and-forth dialogue
- **Real-time Output**: Watch the conversation unfold in real-time

## 🛠️ Prerequisites

- Python 3.13+
- OpenAI API key
- Anthropic API key
- Environment variables configured

## 📦 Installation

1. Install dependencies:
```bash
pip install openai anthropic python-dotenv
```

2. Set up environment variables in `.env`:
```bash
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## 🏃‍♂️ Usage

```bash
python day_5_adversarial_conversation/adversarial_conversation.py
```

## 🎯 What It Does

1. **Initializes Two AI Personas**:
   - GPT with an argumentative, snarky personality
   - Claude with a polite, agreeable personality

2. **Starts Simple Conversation**:
   - GPT: "Hi there"
   - Claude: "Hi"

3. **Runs Adversarial Loop**:
   - GPT responds argumentatively to Claude's message
   - Claude responds politely, trying to find common ground
   - Repeats for 5 rounds

4. **Displays Real-time Dialogue**: Shows the evolving conversation between the two contrasting AI personalities

## 🔧 Configuration

### Model Settings
```python
gpt_model = "gpt-4o-mini"          # OpenAI model
claude_model = "claude-3-haiku-20240307"  # Anthropic model
```

### Personality Prompts
- **GPT System Prompt**: Creates argumentative, challenging behavior
- **Claude System Prompt**: Creates polite, agreeable behavior

## 📊 Example Output

```
GPT:
Hi there

Claude:
Hi

GPT:
Oh great, another generic greeting. How wonderfully original...

Claude:
I appreciate you taking the time to say hello! It's always nice to start a conversation...
```

## 🎓 Learning Outcomes

- **System Prompt Engineering**: See how different prompts create distinct AI personalities
- **Multi-Model Integration**: Learn to work with multiple AI providers simultaneously
- **Conversational AI**: Understand how to maintain context across multiple turns
- **API Management**: Handle different API structures (OpenAI vs Anthropic)

## 🤝 Use Cases

- **AI Personality Research**: Study how system prompts affect AI behavior
- **Entertainment**: Create amusing AI conversations
- **Educational Demos**: Show contrast in AI model responses
- **Prompt Engineering Practice**: Experiment with different personality configurations

## 🔒 Security Notes

- Keep API keys secure in environment variables
- Monitor API usage and costs
- Both OpenAI and Anthropic APIs are paid services

## 📄 License

Part of the AI Agent Course Mini Projects - MIT License
