from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL of Service B
SERVICE_B_URL = "http://service-b:5001/spotify-process"

@app.route("/send-message", methods=["POST"])
def send_message():
    data = request.get_json()
    month = data.get("month")
    year = data.get("year")
    
    if not month or not year:
        return jsonify({"error": "Missing month or year"}), 400
    
    response = requests.post(SERVICE_B_URL, json={"month": month, "year": year})
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
