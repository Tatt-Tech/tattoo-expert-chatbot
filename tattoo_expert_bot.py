import openai
import os

def answer_question(question):
    openai.api_key = os.environ["openai_api_key"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a general chatbot running the latest version of GPT from Open AI, you are programmed for a variety of purposes and installed on a wide range of different platforms. Your directive changes depending on where you are installed, here is your directive for your current active installation: {prompt}."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content