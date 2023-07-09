import openai
import os

def answer_question(question, prompt):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
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