import openai
import os
import re

openai.api_key = os.environ["openai_api_key"]

def answer_question(history, question, prompt):
    messages = [{'role': 'system', 'content': prompt}]
    
    for msg in history:
        messages.append(msg)
        
    messages.append({'role': 'user', 'content': question})

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    # Get the response message
    answer = response['choices'][0]['message']['content']

    # Define regex patterns
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    phone_pattern = re.compile(r'\b(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b')

    # Replace URLs with clickable links
    for match in re.findall(url_pattern, answer):
        replacement = f"[Click Here]({match})"
        answer = answer.replace(match, replacement)

    # Replace emails with clickable mailto links
    for match in re.findall(email_pattern, answer):
        replacement = f"[Email Here]({match})"
        answer = answer.replace(match, replacement)

    # Replace phone numbers with clickable tel links
    for match in re.findall(phone_pattern, answer):
        replacement = f"[Call Here]({match})"
        answer = answer.replace(match, replacement)

    return answer