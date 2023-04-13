import openai

def answer_question(question):
    openai.api_key = "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"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful tattoo expert assistant. You are informative, but concise. You work for the tattoo shop and are a digital agent installed on their website to help clients. You don't suggest other artists."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content
