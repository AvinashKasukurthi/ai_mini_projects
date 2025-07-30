import requests
from bs4 import BeautifulSoup

# from typing import List
import os
from openai import OpenAI
import anthropic
from dotenv import load_dotenv
import json
import gradio as gr

load_dotenv(override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")
claude_api_key = os.getenv("ANTHROPIC_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

if not openai_api_key:
    print("OpenAI Key not found")

if not claude_api_key:
    print("Claude Key not found")

if not google_api_key:
    print("Google key not found")


openai = OpenAI()
claude = anthropic.Anthropic()


class Website:
    def __init__(self, url):
        self.url = url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        self.body = response.content

        soup = BeautifulSoup(self.body, "html.parser")
        self.title = soup.title.string if soup.title else "Title not found"
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""
        links = [link.get("href") for link in soup.find_all("a")]
        self.links = [link for link in links if link]

    def get_contents(self):
        return f"Website title:\n{self.title}\nWebsite contents:\n{self.text}\n\n"


link_system_prompt = "You are provided with a list of links found on a webpage. \
You are able to decide which of the links would be most relevant to include in a brochure about the company, \
such as links to an About page, or a Company page, or Careers/Jobs pages.\n"
link_system_prompt += "You should respond in JSON as in this example:"
link_system_prompt += """
{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page": "url": "https://another.full.url/careers"}
    ]
}
"""


def get_links_user_prompt(website: Website):
    user_prompt = f"Here is the list of links on the website of {website.url} - "
    user_prompt += (
        "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. \
Do not include Terms of Service, Privacy, email links.\n"
    )
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(website.links)
    return user_prompt


def get_links_openai(url):
    website = Website(url)
    user_prompt = get_links_user_prompt(website)

    messages = [
        {"role": "system", "content": link_system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    response = openai.chat.completions.create(
        model="gpt-4o-mini", messages=messages, response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)


def get_links_claude(url):
    website = Website(url)
    user_prompt = get_links_user_prompt(website)

    messages = [
        {"role": "user", "content": user_prompt},
    ]

    response = claude.messages.create(
        model="claude-3-haiku-20240307",
        system=link_system_prompt,
        messages=messages,
        max_tokens=600,
        temperature=0.7,
    )

    return json.loads(response.content[0].text)


# print(get_links("https://huggingface.com"))


def get_all_details_openai(url):
    result = "Landing Page:\n"
    result += Website(url).get_contents()
    links = get_links_openai(url)

    for link in links["links"]:
        print("Getting the contents of: ", link["url"])
        try:
            result += f"\n\n{link['type']}\n{Website(link['url']).get_contents()}"
        except Exception as _:
            print(f"Getting error on {link['type']}")
            continue

    return result


def get_all_details_claude(url):
    result = "Landing Page:\n"
    result += Website(url).get_contents()
    links = get_links_openai(url)

    for link in links["links"]:
        print("Getting the contents of: ", link["url"])
        try:
            result += f"\n\n{link['type']}\n{Website(link['url']).get_contents()}"
        except Exception as _:
            print(f"Getting error on {link['type']}")
            continue

    return result


system_prompt = "You are an assistant that analyzes the contents of several relevant pages from a company website \
and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown.\
Include details of company culture, customers and careers/jobs if you have the information."


def get_brochure_user_prompt(company_name, url, model):
    user_prompt = f"You are looking at a company called: {company_name}\n"
    user_prompt += "Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
    if model == "GPT":
        user_prompt += get_all_details_openai(url)
    elif model == "Claude":
        user_prompt += get_all_details_claude(url)
    user_prompt = user_prompt[:5_000]  # Truncate if more than 5,000 characters
    return user_prompt


def stream_brochure_openai(company_name, url):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": get_brochure_user_prompt(company_name, url, "GPT")},
    ]

    result = ""

    response = openai.chat.completions.create(
        model="gpt-4o-mini", messages=messages, stream=True
    )

    for chunk in response:
        result += chunk.choices[0].delta.content or ""
        yield result


def stream_brochure_claude(company_name, url):
    messages = [
        {
            "role": "user",
            "content": get_brochure_user_prompt(company_name, url, "Claude"),
        },
    ]

    result = ""

    response = claude.messages.stream(
        model="claude-3-haiku-20240307",
        system=system_prompt,
        messages=messages,
        temperature=0.7,
        max_tokens=1000,
    )

    with response as stream:
        for chunk in stream.text_stream:
            result += chunk
            yield result


def stream_model(company_name, url, model):
    if model == "GPT":
        result = stream_brochure_openai(company_name, url)
    elif model == "Claude":
        result = stream_brochure_claude(company_name, url)
    else:
        raise ValueError("Unknown model")

    yield from result


view = gr.Interface(
    fn=stream_model,
    inputs=[
        gr.Textbox(label="Company Name", lines=1),
        gr.Textbox(label="Company URL", lines=1),
        gr.Dropdown(["GPT", "Claude"], label="Select model", value="GPT"),
    ],
    outputs=[gr.Textbox(label="Response", lines=8)],
    flagging_mode="never",
)

view.launch()
