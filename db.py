import sqlite3, time
from flask import g

def get_connection():
    con = sqlite3.connect("database.db")
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

def execute(sql, params=[]):
    retries = 3
    for attempt in range(retries):
        try:
            con = get_connection()
            result = con.execute(sql, params)
            con.commit()
            g.last_insert_id = result.lastrowid
            return result
        except sqlite3.OperationalError as e:
            if "database is locked" in str(e) and attempt < retries - 1:
                print(f"Database is locked. Retrying... (Attempt {attempt + 1})")
                time.sleep(1)
            else:
                raise e
        finally:
            con.close()

def query(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result

def last_insert_id():
    return g.last_insert_id