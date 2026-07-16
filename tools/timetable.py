import sqlite3

DB_PATH = "students.db"

def get_timetable(day):
    print(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT period, subject, faculty FROM timetable WHERE day=?",
        (day,)
    )

    rows = cursor.fetchall()

    conn.close()

    timetable = []

    for row in rows:
        timetable.append({
            "period": row[0],
            "subject": row[1],
            "faculty": row[2]
        })

    return timetable