from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL of Service B
SERVICE_B_URL = "http://service-b:5001/ai-process"

@app.route("/send-message", methods=["POST"])
def send_message():
    data = request.json
    user_text = data.get("text", "")

    if not user_text:
        return jsonify({"error": "No text provided"}), 400

    # Send text to Service B for AI processing
    response = requests.post(SERVICE_B_URL, json={"text": user_text})

    return response.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
