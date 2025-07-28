from openai import OpenAI
import anthropic
from dotenv import load_dotenv

load_dotenv(override=True)

openai = OpenAI()
claude = anthropic.Anthropic()

gpt_model = "gpt-4o-mini" 
claude_model = "claude-3-haiku-20240307"

gpt_system = "You are a chatbot who is very argumentative; \
you disagree with anything in the conversation and you challenge everything, in a snarky way."

claude_system = "You are a very polite, courteous chatbot. You try to agree with \
everything the other person says, or find common ground. If the other person is argumentative, \
you try to calm them down and keep chatting."

gpt_messages = ["Hi there"]
claude_messages = ["Hi"]

def call_gpt():
    messages = [{"role": "system", "content": gpt_system}]

    for gpt, claude_msg in zip(gpt_messages, claude_messages):
        messages.append({"role": "assistant", "content": gpt})
        messages.append({"role": "user", "content": claude_msg})
    
    completion = openai.chat.completions.create(
        model=gpt_model,
        messages=messages
    )

    return completion.choices[0].message.content

def call_claude():
    messages = []
    for gpt, claude_msg in zip(gpt_messages, claude_messages):
        messages.append({'role': 'user', 'content': gpt})
        messages.append({'role': 'assistant', 'content': claude_msg})
    
    messages.append({'role': 'user', 'content': gpt_messages[-1]})
    message = claude.messages.create(
        model=claude_model,
        max_tokens=500,
        system=claude_system,
        messages=messages
    )

    return message.content[0].text

print(f"GPT:\n{gpt_messages[0]}\n")
print(f"Claude:\n{claude_messages[0]}\n")

for i in range(5):
    gpt_next = call_gpt()
    print(f"GPT:\n{gpt_next}\n")
    gpt_messages.append(gpt_next)

    claude_next = call_claude()
    print(f"Claude:\n{claude_next}\n")
    claude_messages.append(claude_next)