from flask import Flask, request, session, jsonify
from flask_cors import CORS
from tattoo_expert_bot import answer_question

app = Flask(__name__)
CORS(app)
app.secret_key = 'openai_api_key'

@app.route('/api/chat', methods=['POST'])
def chat():
    # Load the question and prompt from the POST request
    data = request.get_json()
    question = data['message']
    prompt = data.get('prompt', '')  # The prompt is optional

    # If 'history' is not in the session, initialize it with the prompt
    # This happens the first time the function is called
    if 'history' not in session:
        session['history'] = [{'role': 'system', 'content': prompt}] if prompt else []
        print('Initializing session history')  # Debug line

    print('Current session history:', session['history'])  # Debug line

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