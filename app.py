from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

@app.route("/add", methods=["POST"])
def add_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    existing_data.append(data)

    with open(DATA_FILE, 'w') as f:
        json.dump(existing_data, f, indent=4)

    return jsonify({"message": "Data saved successfully"}), 200
