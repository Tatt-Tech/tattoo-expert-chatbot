import openai
import os

openai.api_key = os.environ["openai_api_key"]

def answer_question(history, question, prompt):
    if not history:
        messages = [{'role': 'system', 'content': prompt}]
    else:
        messages = []
        
    for msg in history:
        messages.append(msg)
        
    messages.append({'role': 'user', 'content': question})

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    return response['choices'][0]['message']['content']