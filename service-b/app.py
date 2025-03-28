import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, jsonify
from config import API_KEY

app = Flask(__name__)

spotipy.api_key = API_KEY

@app.route("/ai-process", methods=["POST"])
def spotify_process():
    return


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
