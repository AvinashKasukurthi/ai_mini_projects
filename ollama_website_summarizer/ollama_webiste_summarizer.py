import ollama
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

MODEL = "llama3.2"


class Website:
    def __init__(self, url):
        website_response = requests.get(url, headers=headers)
        website_content = website_response.content

        website_soup = BeautifulSoup(website_content, "html.parser")
        self.title = (
            website_soup.title.string if website_soup.title else "No title found"
        )
        # Remove the irrelevant content from body
        for irrelevant in website_soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = website_soup.body.get_text(separator="\n", strip=True)


def get_user_prompt(website: Website):
    user_prompt = f"You are looking at website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text

    return user_prompt


def get_messages_for(website: Website):
    SYSTEM_PROMPT = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": get_user_prompt(website)},
    ]

    return messages


def summarize(url):
    website = Website(url)
    response = ollama.chat(model=MODEL, messages=get_messages_for(website))
    return response.message.content


def display(url):
    summary = summarize(url)
    print(summary)


display("https://www.hapsoul.com")
