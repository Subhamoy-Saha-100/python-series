from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# client = OpenAI()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
    model="gpt-6-astra",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general knowledge like alexa and programming. You are helpful, creative, clever, and very friendly."},
        {"role": "user", "content": "What is coding?"},
    ],
)
print(completion.choices[0].message.content)
