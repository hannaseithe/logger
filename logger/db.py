import sqlite3
import datetime

def save_log(log):
    connection = sqlite3.connect("logger.db")
    cursor = connection.cursor()

    sql_create_command = """
    CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY,
    message VARCHAR(500), 
    level VARCHAR(30), 
    ip VARCHAR(100),
    logged_at DATETIME NOT NULL
    );"""

    cursor.execute(sql_create_command)

    now = datetime.datetime.now()

    cursor.execute("""
        INSERT INTO logs (id, message, level, ip, logged_at)
        VALUES (?, ?, ?, ?, ?)
    """, (None, log["message"], log["level"], log["ip"], now))

    connection.commit()
    connection.close()