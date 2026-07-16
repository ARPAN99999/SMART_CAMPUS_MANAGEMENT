import sqlite3

DB_PATH = "students.db"

def upcoming_exams():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT subject, date, time FROM exams"
    )

    rows = cursor.fetchall()

    conn.close()

    exams = []

    for row in rows:
        exams.append({
            "subject": row[0],
            "date": row[1],
            "time": row[2]
        })

    return exams