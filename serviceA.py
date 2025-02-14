# Service A: Flask API for User Interface and Password Management
from flask import Flask, request, jsonify
import jwt
import datetime
import requests
import hashlib

app = Flask(__name__)
SECRET_KEY = "your_secret_key"
SERVICE_B_URL = "http://service-b:5001"

def generate_jwt(username):
    payload = {
        "user": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    data["password"] = hashlib.sha256(data["password"].encode()).hexdigest()
    response = requests.post(f"{SERVICE_B_URL}/register", json=data)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
