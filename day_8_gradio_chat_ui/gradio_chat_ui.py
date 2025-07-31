# import os
from dotenv import load_dotenv
import gradio as gd
from openai import OpenAI

load_dotenv(override=True)

openai = OpenAI()

system_message = (
    "You are a friendly user assistant. Patiently analyse and give reply technically."
)


def chat(message, history):
    messages = [{"role": "system", "content": system_message}]
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})

    messages.append({"role": "user", "content": message})

    stream = openai.chat.completions.create(
        model="gpt-4o-mini", messages=messages, stream=True
    )

    response = ""

    for chunk in stream:
        response += chunk.choices[0].delta.content or ""

        yield response


gd.ChatInterface(fn=chat).launch()
