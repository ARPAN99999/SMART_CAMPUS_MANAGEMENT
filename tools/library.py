import sqlite3

DB_PATH = "students.db"

def borrowed_books(student_id):
    print(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT book_name, due_date FROM library WHERE student_id=?",
        (student_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    books = []

    for row in rows:
        books.append({
            "book": row[0],
            "due": row[1]
        })

    return books