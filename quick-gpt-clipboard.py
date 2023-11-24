from openai import OpenAI
import os

client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

prompt = "Which is the most popular programming language for machine learning?"

completion = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

print(completion.choices[0].message.content)