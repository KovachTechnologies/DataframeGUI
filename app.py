from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Load schema from schema.json
def load_schema():
    with open('schema.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schema')
def get_schema():
    return jsonify(load_schema())

@app.route('/data')
def get_data():
    # Load schema to ensure dummy data matches it
    schema = load_schema()
    # Generate dummy data dynamically based on schema
    dummy_data = [
        {
            key: idx + 1 if schema[key] == "integer" else f"{key.capitalize()} {idx + 1}"
            for key in schema.keys()
        }
        for idx in range(3)  # Generate 3 rows of dummy data
    ]
    return jsonify(dummy_data)

if __name__ == '__main__':
    app.run(debug=True)
