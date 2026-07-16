import sqlite3

DB_PATH = "students.db"

def get_attendance(student_id):
    print(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, attendance FROM students WHERE id=?",
        (student_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return {
            "name": result[0],
            "attendance": result[1]
        }

    return None