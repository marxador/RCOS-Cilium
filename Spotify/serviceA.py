from flask import Flask, redirect, request, jsonify
import requests
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

app = Flask(__name__)

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SCOPE = "user-top-read"

@app.route("/")
def login():
    auth_url = (
        "https://accounts.spotify.com/authorize"
        "?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={urllib.parse.quote(REDIRECT_URI)}"
        f"&scope={urllib.parse.quote(SCOPE)}"
    )
    return redirect(auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    token_url = "https://accounts.spotify.com/api/token"
    body = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": os.getenv("SPOTIPY_CLIENT_SECRET"),
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(token_url, data=body, headers=headers)
    tokens = response.json()
    access_token = tokens.get("access_token")

    return (
        '''
        <form action="/wrapped" method="post">
            <input type="hidden" name="token" value="{0}">
            Month (1–12): <input name="month"><br>
            Year (e.g., 2024): <input name="year"><br>
            <input type="submit" value="Get My Monthly Wrapped">
        </form>
        '''.format(access_token)
    )

@app.route("/wrapped", methods=["POST"])
def get_wrapped():
    access_token = request.form["token"]
    month = request.form["month"]
    year = request.form["year"]

    payload = {
        "access_token": access_token,
        "month": month,
        "year": year,
    }

    res = requests.post("http://localhost:5001/monthly-wrapped", json=payload)
    return jsonify(res.json())

if __name__ == "__main__":
    app.run(port=5000, debug=True)
