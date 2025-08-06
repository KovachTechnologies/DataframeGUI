from flask import Flask, render_template, jsonify
import json
import MySQLdb
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Load credentials from credentials.json
def load_credentials():
    with open('credentials.json', 'r') as f:
        return json.load(f)

# Initialize database connection
def get_db_connection():
    creds = load_credentials()
    return MySQLdb.connect(
        host=creds['hostname'],
        user=creds['username'],
        passwd=creds['password'],
        db=creds['database']
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schema')
def get_schema():
    try:
        creds = load_credentials()
        # Connect to database
        connection = get_db_connection()
        cursor = connection.cursor(MySQLdb.cursors.DictCursor)  # Fetch rows as dictionaries
        # Query one row to get column names and types
        cursor.execute(f"SELECT * FROM {creds['table']} LIMIT 1")
        rows = cursor.fetchall()
        
        if not rows:
            # If table is empty, fetch column names from table schema
            cursor.execute(f"SHOW COLUMNS FROM {creds['table']}")
            columns = cursor.fetchall()
            # Create a dummy schema with generic types (object as fallback)
            schema = {col['Field']: 'object' for col in columns}
        else:
            # Convert single row to DataFrame to infer types
            df = pd.DataFrame(rows)
            schema = {col: str(dtype) for col, dtype in df.dtypes.items()}
        
        cursor.close()
        connection.close()
        return jsonify(schema)
    except Exception as e:
        print(f"Error fetching schema: {e}")
        return jsonify({"error": "Schema fetch error"}), 500

@app.route('/data')
def get_data():
    try:
        creds = load_credentials()
        # Connect to database
        connection = get_db_connection()
        cursor = connection.cursor(MySQLdb.cursors.DictCursor)  # Fetch rows as dictionaries
        # Query all data
        cursor.execute(f"SELECT * FROM {creds['table']}")
        rows = cursor.fetchall()
        
        # Convert to DataFrame
        df = pd.DataFrame(rows)
        
        # Convert datetime columns to string for JSON compatibility
        for col in df.select_dtypes(include=['datetime64[ns]']).columns:
            df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')
        
        # Convert DataFrame to JSON-compatible list of dictionaries
        data = df.to_dict(orient='records')
        
        cursor.close()
        connection.close()
        return jsonify(data)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return jsonify({"error": "Data fetch error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
