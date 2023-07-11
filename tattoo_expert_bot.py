import openai
import os

openai.api_key = 'your_openai_api_key'

def answer_question(history, question):
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}]
    for msg in history:
        messages.append(msg)

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    return response['choices'][0]['message']['content']