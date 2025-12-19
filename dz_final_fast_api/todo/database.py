import sqlite3
import os

DB_DIR = "/app/data"
DB_PATH = os.path.join(DB_DIR, "tasks.db")

def init_db():
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            done INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def get_all():
    conn = sqlite3.connect(DB_PATH)
    items = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return items

def add_item(title, description="", completed=False):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (title, description, done) VALUES (?, ?, ?)",  
        (title, description, 1 if completed else 0)  
    )
    item_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return item_id

def update_item(item_id, done):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("UPDATE items SET done = ? WHERE id = ?", (done, item_id))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()