from tools.faculty import get_faculty
from tools.canteen import get_menu
from tools.exam import upcoming_exams
from tools.navigation import find_location

print(get_faculty("Roy"))
print()

print(get_menu())
print()

print(upcoming_exams())
print()

print(find_location("library"))
