from tools.router import choose_tool

from tools.attendance import get_attendance
from tools.timetable import get_timetable
from tools.library import borrowed_books
from tools.faculty import get_faculty
from tools.exam import upcoming_exams
from tools.canteen import get_menu
from tools.navigation import find_location

from llm import ask_gemini


class SmartCampusAgent:

    def chat(self, query):

        action = choose_tool(query)

        tool = action["tool"]

        args = action["arguments"]

        if tool == "attendance":

            result = get_attendance(args["student_id"])

        elif tool == "timetable":

            result = get_timetable(args["day"])

        elif tool == "library":

            result = borrowed_books(args["student_id"])

        elif tool == "faculty":

            result = get_faculty(args["name"])

        elif tool == "exam":

            result = upcoming_exams()

        elif tool == "canteen":

            result = get_menu()

        elif tool == "navigation":

            result = find_location(args["place"])

        else:

            return ask_gemini(query)

        final_prompt = f"""
User asked:

{query}

Tool Result:

{result}

Answer naturally.
"""

        return ask_gemini(final_prompt)