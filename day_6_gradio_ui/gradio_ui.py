import os
from dotenv import load_dotenv
from openai import OpenAI
import anthropic

from google import genai
from google.genai import types
import gradio as gr

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:8]}")
else:
    print("Google API Key not set")

openai = OpenAI()
claude = anthropic.Anthropic()
google = genai.Client()

system_message = "You are a helpful assistant"


def message_gpt(prompt):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]

    completion = openai.chat.completions.create(
        messages=messages,
        model="gpt-4o-mini",
    )

    return completion.choices[0].message.content


# message_gpt("What is today's date?")


def shout(text):
    return text.upper()


# Test Function
# gr.Interface(fn=shout, inputs="textbox", outputs="textbox").launch()
# gr.Interface(
#     fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never"
# ).launch(share=True)
# gr.Interface(
#     fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never"
# ).launch(inbrowser=True)


system_message = "You are a helpful assistant that responds in markdown"


def stream_gpt(prompt):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]

    stream = openai.chat.completions.create(
        model="gpt-4o-mini", messages=messages, stream=True
    )

    result = ""

    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result


def stream_claude(prompt):
    result = claude.messages.stream(
        model="claude-3-haiku-20240307",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        system=system_message,
        max_tokens=1000,
    )
    response = ""

    with result as stream:
        for text in stream.text_stream:
            response += text or ""
            yield response


def stream_gemini(prompt):
    result = google.models.generate_content_stream(
        config=types.GenerateContentConfig(
            system_instruction=system_message,
        ),
        contents=[prompt],
        model="gemini-2.5-flash",
    )

    response = ""

    for chunk in result:
        response += chunk.text
        yield response


def stream_model(prompt, model):
    if model == "GPT":
        result = stream_gpt(prompt)
    elif model == "Claude":
        result = stream_claude(prompt)
    elif model == "Gemini":
        result = stream_gemini(prompt)
    else:
        raise ValueError("Unknown model")

    yield from result


view = gr.Interface(
    fn=stream_model,
    inputs=[
        gr.Textbox(label="Your Message", lines=6),
        gr.Dropdown(["GPT", "Claude", "Gemini"], label="Select model", value="GPT"),
    ],
    outputs=[gr.Textbox(label="Response", lines=8)],
    flagging_mode="never",
)

view.launch()
