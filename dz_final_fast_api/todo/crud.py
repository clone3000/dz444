from database import get_db_connection

def create_item(title, description=None, completed=False):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO todo_items (title, description, completed)
        VALUES (?, ?, ?)
    ''', (title, description, completed))
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()
    return item_id

def get_all_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM todo_items')
    items = cursor.fetchall()
    conn.close()
    return [dict(item) for item in items]

def get_item_by_id(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM todo_items WHERE id = ?', (item_id,))
    item = cursor.fetchone()
    conn.close()
    return dict(item) if item else None

def update_item(item_id, title=None, description=None, completed=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    updates = []
    params = []
    
    if title is not None:
        updates.append("title = ?")
        params.append(title)
    if description is not None:
        updates.append("description = ?")
        params.append(description)
    if completed is not None:
        updates.append("completed = ?")
        params.append(completed)
    
    params.append(item_id)
    query = f"UPDATE todo_items SET {', '.join(updates)} WHERE id = ?"
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todo_items WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()