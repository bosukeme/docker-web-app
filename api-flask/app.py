import os
from flask import Flask, jsonify
import psycopg2
from psycopg2 import pool


app = Flask(__name__)

# Initialize connection pool
database_url = os.getenv('DATABASE_URL') or "postgres://postgres:foobarbaz@localhost:5432/postgres"
connection_pool = pool.SimpleConnectionPool(1, 20, dsn=database_url)


@app.route('/')
def get_datetime():
    conn = connection_pool.getconn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT NOW() as now;")
            result = cur.fetchone()
            response = {
                'now': result[0],
                'api': 'flask'
            }
            return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        connection_pool.putconn(conn)

@app.route('/ping')
def ping():
    return 'pong'

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

