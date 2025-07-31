import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gd

load_dotenv(override=True)

open_api_key = os.getenv("OPENAI_API_KEY")

if not open_api_key:
    print("Open API Key not found")

MODEL = "gpt-4o-mini"
openai = OpenAI()

system_message = "You are a helpful assistant for an Airline called FlightAI. "
system_message += "Give short, courteous answers, no more then 1 sentence. "
system_message += "Always be accurate. If you don't know the answer. Say so."


def get_ticket_price(destination_city):
    """
    Argument: city
    Return: price_in_rupees
    """
    city_prices = {
        "varanasi": "₹20000",
        "tirupathi": "₹4000",
        "ujjain": "₹8000",
        "ayodhya": "₹9000",
        "madhura": "₹12000",
        "vrindhavan": "₹10000",
        "belur": "₹19000",
    }
    city = destination_city.lower()

    return city_prices.get(city, "Unknown")


price_function = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city. Call this whenever you need to know the ticket price, for example when a customer asks 'How much is a ticket to this city'",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that the customer wants to travel to",
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False,
    },
}

tools = [{"type": "function", "function": price_function}]


def handle_tool_call(message):
    tool_call = message.tool_calls[0]
    arguments = json.loads(tool_call.function.arguments)
    city = arguments.get("destination_city")
    price = get_ticket_price(city)
    response = {
        "role": "tool",
        "content": json.dumps({"destination_city": city, "price": price}),
        "tool_call_id": message.tool_calls[0].id,
    }

    return response, city


def chat(message, history):
    messages = [{"role": "system", "content": system_message}]
    for human, assistant in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": assistant})
    messages.append({"role": "user", "content": message})
    response = openai.chat.completions.create(
        model=MODEL, messages=messages, tools=tools
    )

    if response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        response, city = handle_tool_call(message)
        messages.append(message)
        messages.append(response)
        response = openai.chat.completions.create(model=MODEL, messages=messages)

    return response.choices[0].message.content


gd.ChatInterface(fn=chat).launch()
