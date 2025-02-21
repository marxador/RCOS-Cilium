# Service A: Flask API for User Interface
from flask import Flask, jsonify

app = Flask(__name__) # Initialize the Flask app

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Password Manager!"})

@app.route("/data")
def data():
    return jsonify({"message": "Data will be shown here"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
