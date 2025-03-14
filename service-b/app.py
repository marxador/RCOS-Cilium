from flask import Flask, request, jsonify
import openai
import os
from config import OPENAI_API_KEY

app = Flask(__name__)

openai.api_key = OPENAI_API_KEY

@app.route("/ai-process", methods=["POST"])
def ai_process():
    data = request.json
    user_input = data.get("text", "")

    if not user_input:
        return jsonify({"error": "No text provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        bot_reply = response["choices"][0]["message"]["content"]
        return jsonify({"response": bot_reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
