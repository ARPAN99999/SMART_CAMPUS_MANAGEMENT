from tools.attendance import get_attendance
from tools.timetable import get_timetable
from tools.library import borrowed_books

print(get_attendance(101))
print()

print(get_timetable("Monday"))
print()

print(borrowed_books(101))