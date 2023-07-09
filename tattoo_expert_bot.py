import openai
import os

openai.api_key = os.environ["openai_api_key"]

def answer_question(question, prompt):
    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
            {
                "role": "system",
                "content": prompt  
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )
    return response.choices[0].message['content']