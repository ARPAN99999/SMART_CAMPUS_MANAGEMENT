import sqlite3

DB_PATH = "students.db"

def get_faculty(name):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, department, cabin, email FROM faculty WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return {
            "name": row[0],
            "department": row[1],
            "cabin": row[2],
            "email": row[3]
        }

    return None