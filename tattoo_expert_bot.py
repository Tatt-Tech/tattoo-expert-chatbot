import openai
import os

openai.api_key = os.environ["openai_api_key"]

def answer_question(history, prompt):
    messages = []
    for message in history:
        messages.append(openai.ChatCompletion.Message(
            role=message["role"],
            content=str(message["content"])  # Ensure the content is a string
        ))

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150
    )

    return response['choices'][0]['message']['content']