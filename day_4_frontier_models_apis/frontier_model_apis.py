from openai import OpenAI
import anthropic
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

openai = OpenAI()
claude = anthropic.Anthropic()
google_ai = genai.Client()

if openai_api_key:
    print("OpenAI Key exists")
else:
    print("OpenAI Key not found")

if anthropic_api_key:
    print("Anthropic key exists")
else:
    print("Anthropic Key not found")

if google_api_key:
    print("Google Key exists")
else:
    print("Google Key not found")

system_message = "You are an assistant that is great at telling jokes"
user_prompt = "Tell a light-hearted joke for an audience of Data Scientists"

prompts = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_prompt},
]

response_3_5 = openai.chat.completions.create(
    model="gpt-3.5-turbo", messages=prompts, temperature=0.7
)

response_4o_mini = openai.chat.completions.create(
    model="gpt-4o-mini", messages=prompts, temperature=0.7
)

response_4o = openai.chat.completions.create(
    model="gpt-4o", messages=prompts, temperature=0.7
)


print("\n\n---- GPT 3.5 Turbo ----\n")
print(response_3_5.choices[0].message.content)

print("\n\n---- GPT 4o Mini ----\n")
print(response_4o_mini.choices[0].message.content)

print("\n\n---- GPT 4o ----\n")
print(response_4o.choices[0].message.content)
print("\n\n")

claude_response = claude.messages.create(
    model="claude-3-7-sonnet-latest",
    system=system_message,
    messages=[{"role": "user", "content": user_prompt}],
    temperature=0.7,
    max_tokens=200,
)

print("\n\n---- Claude Sonnet 3.7 ----\n")
print(claude_response.content[0].text)
print("\n\n")

gemini_response = google_ai.models.generate_content(
    config=types.GenerateContentConfig(
        system_instruction=system_message, temperature=0.7
    ),
    model="gemini-2.5-flash",
    contents=[user_prompt],
)

print("\n\n---- Google Gemini 2.5 Flash ----\n")
print(gemini_response.text)
print("\n\n")
