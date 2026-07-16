import sqlite3

DB_PATH = "students.db"

def get_menu():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT item, price FROM canteen")

    rows = cursor.fetchall()

    conn.close()

    menu = []

    for row in rows:
        menu.append({
            "item": row[0],
            "price": row[1]
        })

    return menu