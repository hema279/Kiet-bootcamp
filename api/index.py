from flask import Flask, request, jsonify, send_from_directory
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
DB_URL = "postgresql://neondb_owner:npg_4Ekf1QgBIzbe@ep-calm-brook-aigck6rq-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require"

@app.route('/api/students')
def get_students():
    # Fetch ALL 600 students so frontend search works instantly
    with psycopg2.connect(DB_URL) as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM bootcamp_feedback ORDER BY id ASC LIMIT 600;") 
        return jsonify(cur.fetchall())

@app.route('/')
def home(): return send_from_directory('../public', 'index.html')

@app.route('/images/<path:filename>')
def serve_image(filename): return send_from_directory('../public/images', filename)

if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
