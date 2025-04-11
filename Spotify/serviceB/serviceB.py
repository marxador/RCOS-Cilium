from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/monthly-wrapped", methods=["POST"])
def monthly_wrapped():
    data = request.get_json()
    token = data["access_token"]
    month = int(data["month"])
    year = int(data["year"])

    # Spotify does not provide month filtering directly, so this is a rough simulation
    headers = {"Authorization": f"Bearer {token}"}
    endpoint = "https://api.spotify.com/v1/me/top/tracks?limit=10&time_range=short_term"
    
    response = requests.get(endpoint, headers=headers)
    if response.status_code != 200:
        return {"error": "Failed to fetch data from Spotify"}, 500

    tracks = response.json().get("items", [])
    track_summary = [
        {"name": t["name"], "artist": t["artists"][0]["name"]} for t in tracks
    ]

    return {
        "month": month,
        "year": year,
        "top_tracks": track_summary,
        "note": "Spotify does not provide per-month breakdowns via API. This is based on 'short_term' (last ~4 weeks)."
    }

if __name__ == "__main__":
    app.run(port=5001, debug=True)
