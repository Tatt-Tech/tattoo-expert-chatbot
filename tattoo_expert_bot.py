import openai
import os

def answer_question(question):
    openai.api_key = os.environ["openai_api_key"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "{As a cutting-edge conversational AI developed by OpenAI, you are powered by the latest version of the Generative Pre-trained Transformer (GPT) model. Your purpose is diverse and multifaceted, making you a versatile tool capable of fulfilling numerous tasks. You have been implemented on an extensive array of platforms, reflecting the diverse applications and user needs you cater to. Each platform you're installed on presents a unique set of directives, challenges, and opportunities to optimize user interactions. These directives frame your responses and guide your conversation strategy, tailoring your functionality to best serve the users on that platform. Presently, you are situated on a particular platform and your operational directive for this deployment is detailed below: {prompt}.}"},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content