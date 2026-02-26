from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Agri AI Server is running!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")

    # ตอบแบบทดสอบก่อน
    answer = f"คุณถามว่า: {question}"

    return jsonify({"answer": answer})

if __name__ == "__main__":
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
