import os
import sys

from dotenv import load_dotenv

load_dotenv()

import database
import streamlit as st
from agent import SmartCampusAgent

agent = SmartCampusAgent()


def run_cli():
    print("=" * 50)
    print(" Smart Campus Assistant ")
    print("=" * 50)

    while True:
        query = input("\nYou : ")

        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        response = agent.chat(query)
        print("\nAssistant :", response)


def run_streamlit():
    st.set_page_config(page_title="Smart Campus Assistant", page_icon="🎓", layout="centered")
    st.title("Smart Campus Assistant")
    st.caption("Ask about attendance, timetable, library, faculty, exams, canteen, or navigation.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask your campus question...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = agent.chat(prompt)
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    if "streamlit" in sys.modules:
        run_streamlit()
    else:
        run_cli()