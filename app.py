from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Database connection
conn = psycopg2.connect(
    dbname='your_db_name',
    user='your_db_user',
    password='your_db_password',
    host='your_db_host',
    port='your_db_port'
)

# Endpoint to fetch time-series data
@app.route('/timeseries', methods=['GET'])
def get_time_series():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM time_series_data;')
    rows = cursor.fetchall()
    cursor.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
