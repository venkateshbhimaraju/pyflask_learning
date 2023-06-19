from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def create_sqlite_conn():
    conn = sqlite3.connect('database.db')
    return conn

def db_execute_ddl_dml(conn, query, params=None):
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()

def db_execute_select(conn, query, params=None):
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    rows = cursor.fetchall()
    return rows

@app.route('/')
def home():
    conn = create_sqlite_conn()
    result = db_execute_select(conn, "SELECT * FROM users")
    conn.close()
    return render_template('data_render.html', data=result)

if __name__ == '__main__':
    app.run(port=5001)

