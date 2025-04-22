from flask import Flask, render_template, redirect, request, jsonify
import requests
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

app = Flask(__name__)

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SCOPE = "user-top-read"

# Landing page with login button
@app.route("/")
def home():
    return render_template("index.html")

# Redirect to Spotify OAuth
@app.route("/login")
def login():
    auth_url = (
        "https://accounts.spotify.com/authorize"
        "?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={urllib.parse.quote(REDIRECT_URI)}"
        f"&scope={urllib.parse.quote(SCOPE)}"
    )
    return redirect(auth_url)

# Spotify callback after login
@app.route("/callback")
def callback():
    code = request.args.get("code")
    token_url = "https://accounts.spotify.com/api/token"
    body = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(token_url, data=body, headers=headers)
    tokens = response.json()
    access_token = tokens.get("access_token")

    # Show form with access_token hidden in input
    return render_template("form.html", token=access_token)

# Handle form submission and display results
@app.route("/wrapped", methods=["POST"])
def get_wrapped():
    access_token = request.form["token"]
    time_range = request.form["range"]  # short_term, medium_term, or long_term

    payload = {
        "access_token": access_token,
        "range": time_range,
    }

    res = requests.post("http://localhost:5001/monthly-wrapped", json=payload)
    result = res.json()

    return render_template("results.html", data=result)
if __name__ == "__main__":
    app.run(port=5000, debug=True)
