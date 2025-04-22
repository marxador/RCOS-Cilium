from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/monthly-wrapped", methods=["POST"])
def monthly_wrapped():
    data = request.get_json()
    token = data["access_token"]
    time_range = data.get("range", "short_term")  # fallback to short_term

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"https://api.spotify.com/v1/me/top/tracks?limit=10&time_range={time_range}",
        headers=headers
    )

    if response.status_code != 200:
        return {"error": "Spotify API call failed"}, 500

    tracks = response.json().get("items", [])
    return {
        "range": time_range,
        "top_tracks": [
            {"name": t["name"], "artist": t["artists"][0]["name"]}
            for t in tracks
        ],
        "note": f"Spotify Wrapped for time range: {time_range}"
    }


if __name__ == "__main__":
    app.run(port=5001, debug=True)
