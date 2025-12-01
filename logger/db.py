import sqlite3
import datetime

LEVELS = ["info", "error", "debug", "warning"]

def valid_log(log):
    if not (log["message"] and log["level"] and log["ip"]):
        return False
    message = log["message"]
    level = log["level"]
    ip = log["ip"]
    if not (isinstance(message, str) and isinstance(level, str) and isinstance(ip,str)):
        return False
    if len(message) > 500 or len(level) > 30 or len(ip) > 100:
        return False
    if level not in LEVELS:
        return False
    return True

def save_log(log):
    if valid_log(log): 
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
        print("Log saved")
        return 200
    else:
        return 400