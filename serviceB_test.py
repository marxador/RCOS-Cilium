# Service B: Flask API for Backend use
from flask import Flask, jsonify
import requests

app = Flask(__name__)

SERVICE_A_URL = "http://127.0.0.1:5000/data"

@app.route("/fetch")
def fetch_data():
    try:
        response = requests.get(SERVICE_A_URL)  # Request data from Service A
        data = response.json()
        return jsonify({"service_a_data": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # Run on port 5001
