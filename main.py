from flask import Flask, request, session, jsonify
from tattoo_expert_bot import answer_question

app = Flask(__name__)
app.secret_key = 'openai_api_key'

@app.route('/api/chat', methods=['POST'])
def chat():
    # Load the question from the POST request
    question = request.get_json()['message']

    # If 'history' is not in the session, initialize it
    # This happens the first time the function is called
    if 'history' not in session:
        session['history'] = []

    # Call the function to generate the answer
    answer = answer_question(session['history'], question)

    # Add the question and answer to the history
    session['history'].append({'role': 'user', 'content': question})
    session['history'].append({'role': 'assistant', 'content': answer})

    # Save the session
    session.modified = True

    # Return the answer
    return jsonify({'message': answer})

if __name__ == '__main__':
    app.run(debug=True)