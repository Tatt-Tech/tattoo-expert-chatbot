from flask import Flask, request, session, jsonify
from flask_cors import CORS
from tattoo_expert_bot import answer_question

app = Flask(__name__)
CORS(app)
app.secret_key = 'openai_api_key'

@app.route('/api/chat', methods=['POST'])
def chat():
    # Load the question, prompt, and history from the POST request
    data = request.get_json()
    question = data['message']
    prompt = data.get('prompt', '')  # The prompt is optional
    history = data.get('history', [])  # The history is optional

    print('Current session history:', history)  # Debug line

    # Call the function to generate the answer
    answer = answer_question(history, question)

    # Add the question and answer to the history
    history.append({'role': 'user', 'content': question})
    history.append({'role': 'assistant', 'content': answer})

    # Return the answer
    return jsonify({'message': answer})

if __name__ == '__main__':
    app.run(debug=True)