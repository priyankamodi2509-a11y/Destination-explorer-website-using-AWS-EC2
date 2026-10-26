from flask_cors import CORS
import os
import sqlite3
from datetime import date
from pathlib import Path
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:5500",
            "http://127.0.0.1:5500"
        ]
    }
})
DB_PATH = Path(os.environ.get("BOOKINGS_DB", "/opt/destination-explorer/data/bookings.db"))
CITIES = {"Delhi", "Goa", "Mumbai", "Pune", "Indore", "Chennai", "Chandigarh"}
PACKAGES = {
    "Beach Paradise": ("Goa", 15000),
    "Luxury Goa Trip": ("Goa", 25000),
    "Snow Adventure": ("Manali", 18000),
    "Backwater Bliss": ("Kerala", 20000),
    "Royal Rajasthan": ("Jaipur", 17000),
}

def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        booking_type TEXT NOT NULL,
        origin TEXT,
        destination TEXT NOT NULL,
        travel_date TEXT,
        package_name TEXT,
        price_inr INTEGER,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )""")
    return conn

@app.get('/api/health')
def health():
    return jsonify(status='ok')

@app.post('/api/bookings')
def create_booking():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error='Send JSON booking details.'), 400
    kind = data.get('type')
    if kind == 'flight':
        origin, destination, travel_date = (data.get(k) for k in ('from', 'to', 'date'))
        if origin not in CITIES or destination not in CITIES or origin == destination:
            return jsonify(error='Select different valid departure and destination cities.'), 400
        try:
            if date.fromisoformat(str(travel_date)) < date.today():
                raise ValueError()
        except (ValueError, TypeError):
            return jsonify(error='Choose a valid date today or later.'), 400
        package_name, price = None, None
    elif kind == 'package':
        package_name = data.get('name')
        if package_name not in PACKAGES:
            return jsonify(error='Unknown holiday package.'), 400
        destination, price = PACKAGES[package_name]
        origin, travel_date = None, None
    else:
        return jsonify(error='Booking type must be flight or package.'), 400
    with connect() as conn:
        cursor = conn.execute(
            'INSERT INTO bookings (booking_type, origin, destination, travel_date, package_name, price_inr) VALUES (?, ?, ?, ?, ?, ?)',
            (kind, origin, destination, travel_date, package_name, price))
        booking_id = cursor.lastrowid
    return jsonify(message='Booking saved successfully', booking_id=booking_id), 201

if __name__ == '__main__':
    # Local testing only; use gunicorn on EC2, not Flask's development server.
    app.run(host='127.0.0.1', port=8000)
