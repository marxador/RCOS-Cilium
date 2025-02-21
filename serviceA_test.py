# Service A: Flask API for User Interface
from flask import Flask, jsonify

app = Flask(__name__) # Initialize the Flask app

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Password Manager!"})

@app.route("/data")
def data():
    sample_data = {"user": "John Doe", "site": "www.amazon.com", "password": "password123"}
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
