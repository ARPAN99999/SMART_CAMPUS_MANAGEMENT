import json
import re

from llm import ask_gemini

# Student name to ID mapping
STUDENT_MAP = {
    "arpan": 101,
    "avijit": 102,
    "aritra": 103,
    "arpita": 104,
    "mahato": 105,
    "mahto": 105,  # Alternative spelling
}

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def extract_student_id(query):
    """Extract student name from query and return student ID"""
    text = query.lower()
    for student_name, student_id in STUDENT_MAP.items():
        if student_name in text:
            return student_id
    return 101  # Default to Arpan if no student found

def extract_day(query):
    """Extract day of week from query"""
    text = query.lower()
    for day in DAYS:
        if day in text:
            return day.capitalize()
    return "Monday"  # Default to Monday

def extract_location(query):
    """Extract location from query"""
    text = query.lower()
    locations = ["library", "canteen", "lab", "office", "building", "block", "room", "computer lab", "principal office", "accounts office", "it department"]
    for location in locations:
        if location in text:
            return location
    return "library"  # Default to library

def choose_tool(query):
    text = (query or "").lower()

    if re.search(r"attendance|attend", text):
        student_id = extract_student_id(query)
        return {"tool": "attendance", "arguments": {"student_id": student_id}}

    if re.search(r"timetable|schedule|class", text):
        day = extract_day(query)
        return {"tool": "timetable", "arguments": {"day": day}}

    if re.search(r"library|book|borrow", text):
        student_id = extract_student_id(query)
        return {"tool": "library", "arguments": {"student_id": student_id}}

    if re.search(r"faculty|teacher|professor|staff", text):
        return {"tool": "faculty", "arguments": {"name": "Dr"}}

    if re.search(r"exam|test|upcoming", text):
        return {"tool": "exam", "arguments": {}}

    if re.search(r"canteen|food|menu|lunch|dinner|coffee|sandwich", text):
        return {"tool": "canteen", "arguments": {}}

    if re.search(r"navigation|location|where|room|building|lab", text):
        location = extract_location(query)
        return {"tool": "navigation", "arguments": {"place": location}}

    return {"tool": "chat", "arguments": {}}