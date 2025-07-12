import requests
# from bs4 import BeautifulSoup

OLLAMA_API = "http://localhost:11434/api/chat/"
HEADERS = {
    "Content-Type": "application/json",
}
MODEL = "llama3.2"

messages = [
    {
        "role": "user",
        "content": "Describe some of the best applications of AI in business.",
    },
]

payload = {
    "model": MODEL,
    "messages": messages,
    "stream": False,
}

response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
print("Status Code:", response.status_code)
if response.status_code == 200:
    data = response.json()
    print("Response:", data["message"]["content"])
