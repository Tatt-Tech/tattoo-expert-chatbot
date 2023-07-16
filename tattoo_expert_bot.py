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

    # Replace URLs, emails, and phone numbers with clickable links
    answer = url_pattern.sub(r'<a href="\g<0>">\g<0></a>', answer)
    answer = email_pattern.sub(r'<a href="mailto:\g<0>">\g<0></a>', answer)
    answer = phone_pattern.sub(r'<a href="tel:\g<0>">\g<0></a>', answer)

    # Format the business address correctly
    address_pattern = re.compile(r'"https://goo.gl/maps/xSbf4UPEXe4NKqYu6" target="_blank">Twin Falls, ID USA')
    answer = address_pattern.sub(r'<a href="https://goo.gl/maps/xSbf4UPEXe4NKqYu6" target="_blank">Twin Falls, ID USA</a>', answer)

    return answer