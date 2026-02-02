from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_USER = "appuser"
DB_PASS = "StrongPassword123"
DB_NAME = "appdb"

@app.route("/")
def home():
    return "Backend connected securely via NetBird"

@app.route("/db")
def db_check():
    conn = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        dbname=DB_NAME,
        sslmode="require"
    )
    conn.close()
    return "Database connected successfully!"

app.run(host="0.0.0.0", port=5000)
