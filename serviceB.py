# Service B: Flask API for Data Storage and Management
from flask import Flask, request, jsonify
import sqlite3

service_b_app = Flask(__name__)
DATABASE = "password_manager.db"

# Initialize the database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        site TEXT NOT NULL,
        encrypted_password TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

@service_b_app.route("/register", methods=["POST"])
def service_b_register():
    data = request.json
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (data["username"], data["password"]))
        conn.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "User already exists"}), 400
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()
    service_b_app.run(host="0.0.0.0", port=5001)
