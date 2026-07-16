import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Student Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY,
name TEXT,
department TEXT,
semester INTEGER,
attendance REAL
)
""")

# Timetable
cursor.execute("""
CREATE TABLE IF NOT EXISTS timetable(
day TEXT,
period TEXT,
subject TEXT,
faculty TEXT
)
""")

# Library
cursor.execute("""
CREATE TABLE IF NOT EXISTS library(
student_id INTEGER,
book_name TEXT,
due_date TEXT
)
""")

# Faculty
cursor.execute("""
CREATE TABLE IF NOT EXISTS faculty(
name TEXT,
department TEXT,
cabin TEXT,
email TEXT
)
""")

# Exams
cursor.execute("""
CREATE TABLE IF NOT EXISTS exams(
subject TEXT,
date TEXT,
time TEXT
)
""")

# Canteen
cursor.execute("""
CREATE TABLE IF NOT EXISTS canteen(
item TEXT,
price INTEGER
)
""")

conn.commit()

# -----------------------
# Sample Data
# -----------------------

cursor.execute("DELETE FROM students")
cursor.execute("DELETE FROM timetable")
cursor.execute("DELETE FROM library")
cursor.execute("DELETE FROM faculty")
cursor.execute("DELETE FROM exams")
cursor.execute("DELETE FROM canteen")

cursor.executemany("""
INSERT INTO students
VALUES(?,?,?,?,?)
""",[
(101,"Arpan","Information Technology",4,89.5),
(102,"Avijit","Computer Science",5,91.2),
(103,"Aritra","Electronics",3,84.6),
(104,"Arpita","Information Technology",4,92.1),
(105,"Mahato","Mechanical",2,78.3)
])

cursor.executemany("""
INSERT INTO timetable
VALUES(?,?,?,?)
""",[
("Monday","9:00","Python","Dr. Roy"),
("Monday","10:00","DBMS","Dr. Sen"),
("Tuesday","9:00","Operating System","Dr. Das")
])

cursor.executemany("""
INSERT INTO library
VALUES(?,?,?)
""",[
(101,"Python Crash Course","25 July"),
(101,"Operating System Concepts","30 July"),
(102,"Data Science Handbook","28 July"),
(103,"Digital Systems","27 July"),
(104,"AI: A Modern Approach","01 Aug"),
(105,"Mechanics of Materials","03 Aug")
])

cursor.executemany("""
INSERT INTO faculty
VALUES(?,?,?,?)
""",[
("Dr. Roy","IT","Room 204","roy@college.edu"),
("Dr. Sen","IT","Room 206","sen@college.edu")
])

cursor.executemany("""
INSERT INTO exams
VALUES(?,?,?)
""",[
("DBMS","15 August","10:00 AM"),
("Python","20 August","2:00 PM")
])

cursor.executemany("""
INSERT INTO canteen
VALUES(?,?)
""",[
("Veg Sandwich",40),
("Chicken Roll",70),
("Coffee",20)
])

conn.commit()

print("Database Created Successfully!")

conn.close()