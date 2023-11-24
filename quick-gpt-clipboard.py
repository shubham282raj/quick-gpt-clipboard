from openai import OpenAI
import os

client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

def get_content(prompt):
    completion = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

promt = input("Ask something?")

print(get_content(promt))