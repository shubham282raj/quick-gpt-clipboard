from openai import OpenAI
import os
import pyperclip

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

lastPrompt = 'init'
while(True):
    prompt = pyperclip.paste()
    if(prompt != lastPrompt):
        print("Searching, Please Wait!")

        response = get_content(prompt)
        pyperclip.copy(response)
        lastPrompt = response

        print(response)
        print("\nWaiting for you to copy again\n")