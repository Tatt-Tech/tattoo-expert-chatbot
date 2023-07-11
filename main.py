from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS  
from tattoo_expert_bot import answer_question
from flask_session import Session  # added for server-side sessions

app = Flask(__name__)
CORS(app)
app.config["SESSION_TYPE"] = "filesystem"  # server-side session
Session(app)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    message = request.json["message"]
    prompt = request.json["prompt"]

    # Check if conversation history exists in the session
    if 'history' not in session:
        session['history'] = []

    # If the special command "/clear" is received, clear the conversation history
    if message.strip() == "/clear":
        session['history'] = []
        return jsonify({"answer": "Conversation cleared."})

    # Add the user's message to the conversation history
    session['history'].append({
        "role": "user",
        "content": message
    })

    # Call the OpenAI API with the conversation history
    answer = answer_question(session['history'], prompt)

    # Add the model's response to the conversation history
    session['history'].append({
        "role": "assistant",
        "content": answer
    })

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)