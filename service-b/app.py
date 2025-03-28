import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, jsonify
from config import API_KEY, API_SECRET, REDIRECT_URI

app = Flask(__name__)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=API_KEY,
    client_secret=API_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-top-read"
))

@app.route("/spotify-process", methods=["POST"])
def spotify_process():
    data = request.get_json()
    month = data.get("month")
    year = data.get("year")

    if not month or not year:
        return jsonify({"error": "Missing month or year"}), 400

    results = sp.current_user_top_tracks(time_range="short_term", limit=10)
    top_tracks = [{"name": track["name"], "artist": track["artists"][0]["name"]} for track in results["items"]]

    return jsonify({"month": month, "year": year, "top_tracks": top_tracks})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
