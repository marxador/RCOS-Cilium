from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL of Service B
SERVICE_B_URL = "http://service-b:5001/spotify-process"

@app.route("/send-message", methods=["POST"])
def send_message():
    return 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
