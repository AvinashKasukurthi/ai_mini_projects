# Day 9: Airline AI Assistant

An intelligent airline customer service assistant built with Gradio and OpenAI's function calling capabilities. This project demonstrates how to create a specialized AI assistant that can handle ticket price inquiries for FlightAI airline using structured function calls.

## 🌟 Features

- **Function Calling Integration**: Uses OpenAI's function calling to retrieve real-time ticket prices
- **Airline-Specific Assistant**: Customized for FlightAI with professional airline customer service persona
- **Interactive Chat Interface**: Clean Gradio-based web interface for customer interactions
- **Multi-City Support**: Covers popular Indian pilgrimage and tourist destinations
- **Structured Responses**: Short, courteous, and accurate responses following airline standards
- **Tool Integration**: Seamless integration between natural language and structured data retrieval

## 🎯 What It Does

The AI assistant can:
- Answer questions about ticket prices to various destinations
- Provide customer service in a professional airline context
- Handle natural language queries and convert them to structured function calls
- Maintain conversation context throughout the interaction
- Give accurate, concise responses following airline customer service standards

## 🚀 How to Run

1. **Set up your OpenAI API key** in a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

2. **Run the application**:
   ```bash
   python day_9_airline_ai_assistant/airline_ai_assistant.py
   ```

3. **Open your browser** and navigate to the provided local URL (typically `http://localhost:7860`)

4. **Start asking about flight prices** to supported destinations!

## 🏙️ Supported Destinations

The assistant currently supports ticket price inquiries for:

| Destination | Price (Return Ticket) |
|-------------|----------------------|
| Varanasi    | ₹20,000             |
| Tirupathi   | ₹4,000              |
| Ujjain      | ₹8,000              |
| Ayodhya     | ₹9,000              |
| Mathura     | ₹12,000             |
| Vrindavan   | ₹10,000             |
| Belur       | ₹19,000             |

## 💡 Key Technical Features

### Function Calling Implementation
The assistant uses OpenAI's function calling to retrieve structured data:
```python
price_function = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city...",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that the customer wants to travel to",
            },
        },
        "required": ["destination_city"],
    },
}
```

### Intelligent Tool Handling
Seamlessly processes function calls and integrates responses:
```python
def handle_tool_call(message):
    tool_call = message.tool_calls[0]
    arguments = json.loads(tool_call.function.arguments)
    city = arguments.get("destination_city")
    price = get_ticket_price(city)
    # Returns structured response for the AI to process
```

### Professional Airline Persona
Configured with specific guidelines for airline customer service:
```python
system_message = "You are a helpful assistant for an Airline called FlightAI. "
system_message += "Give short, courteous answers, no more then 1 sentence. "
system_message += "Always be accurate. If you don't know the answer. Say so."
```

## 🔧 Configuration

### Model Selection
Currently uses GPT-4o-mini for optimal performance and cost efficiency:
```python
MODEL = "gpt-4o-mini"
```

### Adding New Destinations
Easily expand the supported cities by updating the `city_prices` dictionary:
```python
city_prices = {
    "new_city": "₹price",
    # Add more destinations here
}
```

## 📋 Prerequisites

- Python 3.13+
- OpenAI API key
- Required packages:
  - `openai` - OpenAI API client with function calling support
  - `gradio` - Web interface framework
  - `python-dotenv` - Environment variable management

## 🎨 User Experience

- **Natural Language Interface**: Ask questions like "How much is a ticket to Varanasi?"
- **Instant Responses**: Function calls provide immediate price information
- **Professional Service**: Airline-appropriate tone and response format
- **Error Handling**: Graceful handling of unsupported destinations
- **Conversation Flow**: Maintains context for follow-up questions

## 🔍 Example Interactions

**User**: "What's the price for a ticket to Tirupathi?"
**Assistant**: "A return ticket to Tirupathi costs ₹4,000."

**User**: "How much to visit Ayodhya?"
**Assistant**: "The return ticket price to Ayodhya is ₹9,000."

**User**: "Do you have flights to Paris?"
**Assistant**: "I don't have pricing information for Paris in our current system."

## 🚀 Potential Enhancements

- **Dynamic Pricing**: Integrate with real airline pricing APIs
- **Booking Functionality**: Add actual ticket booking capabilities
- **Flight Schedules**: Include departure times and flight duration information
- **Seat Selection**: Add seat availability and selection features
- **Multi-Language Support**: Support regional languages for Indian destinations
- **Payment Integration**: Include payment processing capabilities
- **Loyalty Program**: Add frequent flyer program integration
- **Real-time Updates**: Include flight status and delay information

## 🛠️ Technical Architecture

1. **Frontend**: Gradio ChatInterface for user interaction
2. **Backend**: OpenAI GPT-4o-mini with function calling
3. **Data Layer**: Static pricing dictionary (easily replaceable with database)
4. **Integration**: Seamless tool calling and response handling

## 📊 Business Applications

- **Customer Service Automation**: Reduce human agent workload for basic inquiries
- **24/7 Availability**: Provide round-the-clock customer support
- **Scalable Support**: Handle multiple customers simultaneously
- **Consistent Service**: Ensure uniform response quality across all interactions
- **Data Collection**: Gather insights on popular destinations and pricing inquiries

---

*Part of the AI Agent Course - Day 9: Building specialized AI assistants with function calling capabilities for business applications.*
