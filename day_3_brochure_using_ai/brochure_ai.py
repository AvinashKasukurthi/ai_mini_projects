import os
from dotenv import load_dotenv
import json
import requests
from bs4 import BeautifulSoup
import ollama
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

MODEL = "llama3.2"


class Website:
    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)
        self.body = response.content

        soup = BeautifulSoup(self.body, "html.parser")
        self.title = soup.title.string if soup.title else "No title found"
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


# website = Website("https://huggingface.com")
# print(website.links)


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


def get_links(url):
    website = Website(url)
    user_prompt = get_links_user_prompt(website)

    messages = [
        {"role": "system", "content": link_system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    response = ollama.chat(model=MODEL, messages=messages, format="json")

    return json.loads(response.message.content)


# print(get_links("https://huggingface.com"))


def get_all_details(url):
    result = "Landing Page:\n"
    result += Website(url).get_contents()
    links = get_links(url)

    for link in links["links"]:
        print("Getting the contents of: ", link["url"])
        try:
            result += f"\n\n{link['type']}\n{Website(link['url']).get_contents()}"
        except Exception as e:
            print(f"Getting error on {link['type']}")
            continue

    return result


system_prompt = "You are an assistant that analyzes the contents of several relevant pages from a company website \
and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown.\
Include details of company culture, customers and careers/jobs if you have the information."


def get_brochure_user_prompt(company_name, url):
    user_prompt = f"You are looking at a company called: {company_name}\n"
    user_prompt += "Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
    user_prompt += get_all_details(url)
    user_prompt = user_prompt[:5_000]  # Truncate if more than 5,000 characters
    return user_prompt


def create_brochure(company_name, url):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)},
        ],
    )

    return response.message.content


def stream_brochure(company_name, url):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)},
        ],
        stream=True,
    )

    console = Console()
    accumulated_content = ""

    with Live(console=console, refresh_per_second=10) as live:
        for chunk in response:
            if chunk.message and chunk.message.content:
                accumulated_content += chunk.message.content
                markdown = Markdown(accumulated_content)
                live.update(markdown)
        # console.log(response.us)

    console.print("\n" + "=" * 50)
    console.print("✅ Brochure generation complete!")


stream_brochure("Anthropic", "https://www.anthropic.com/")
