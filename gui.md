##  Spotify Wrapped (Yearly) — Flask + Bootstrap App

This guide documents how to build a simplified, GUI-based Spotify Wrapped web app using **Flask**, **Bootstrap**, and **Spotify's API**. It replaces the React frontend with classic HTML templates for easier development and cleaner integration.

---

##  Project Structure
```
Spotify/
├── serviceA.py                 # Flask app that handles UI, login, and API logic
├── serviceB.py                 # Flask microservice that fetches top tracks from Spotify
├── .env                        # Stores your Spotify credentials
├── templates/
│   ├── index.html              # Landing page with login button
│   ├── form.html               # Time range selection form
│   └── results.html            # Displays top tracks
```

---

##  Step 1: Setup Environment

1. **Install dependencies**:
```bash
pip install flask requests python-dotenv
```

2. **Create `.env` file** with your Spotify app credentials:
```env
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:5000/callback
```
Make sure the redirect URI is also added in your Spotify Developer Dashboard.

---

##  Step 2: Run the App

1. **Start serviceB** in one terminal:
```bash
python serviceB.py
```

2. **Start serviceA** in a second terminal:
```bash
python serviceA.py
```

3. Open your browser and visit:
```
http://localhost:5000
```

You’ll be taken through a Spotify login flow, then asked to choose a time range. Results will display your top tracks for that range.

---

##  Step 3: HTML Template Overview

### `index.html`
- Landing page with a Bootstrap-styled login button.

### `form.html`
- Presents a dropdown for users to select a time range:
  - **short_term** → last 4 weeks
  - **medium_term** → last 6 months
  - **long_term** → 1+ years

### `results.html`
- Shows a list of your top 10 tracks with a heading like:
  > Your Wrapped for the last 6 months

---

##  API Flow Summary

1. User logs in via Spotify OAuth
2. Spotify redirects to `/callback` with an access code
3. `serviceA.py` exchanges the code for an access token
4. User selects a time range via `/form.html`
5. Form posts to `/wrapped`, which calls `serviceB.py`
6. `serviceB.py` calls Spotify's `top tracks` API and returns JSON
7. `serviceA.py` renders `results.html` with the data

---

##  Benefits of This Approach
- Simple, beginner-friendly GUI (HTML + Bootstrap)
- No need for React or Node.js
- Runs on pure Python + Flask
- Easy to deploy and maintain

---

##  Future Improvements
- Add album art or preview links
- Support top **artists** in addition to tracks
- Use charts (e.g. pie chart for genres)
- Save user data to a database for historical stats