from flask import Flask, request, jsonify, render_template
from tattoo_expert_bot import answer_question

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    message = request.json["message"]
    answer = answer_question(message)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
