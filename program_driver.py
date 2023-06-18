import sqlite3
from flask import Flask, render_template

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

def main():
    conn = create_sqlite_conn()
    db_execute_ddl_dml(conn, "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    db_execute_ddl_dml(conn, "INSERT INTO users (username, password) VALUES (?, ?)", ('john', 'password123'))
    result = db_execute_select(conn, "SELECT * FROM users")
    for row in result:
        print(row)

    conn.close()



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


if __name__ == "__main__":
    main()