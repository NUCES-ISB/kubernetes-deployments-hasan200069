from flask import Flask, jsonify
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

app = Flask(__name__)

# Database configuration
DB_USER = os.environ.get('POSTGRES_USER', 'postgres')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
DB_HOST = os.environ.get('POSTGRES_HOST', 'postgres')
DB_PORT = os.environ.get('POSTGRES_PORT', '5432')
DB_NAME = os.environ.get('POSTGRES_DB', 'postgres')

# Create database URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Flask-Kubernetes App!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/db-test')
def db_test():
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        connection.close()
        return jsonify({"status": "Database connection successful!"})
    except OperationalError as e:
        return jsonify({"status": "Database connection failed!", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 