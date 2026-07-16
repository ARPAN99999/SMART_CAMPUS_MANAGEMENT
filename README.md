# 🎓 Smart Campus AI Agent

An intelligent AI-powered campus assistant built using **Python**, **Streamlit**, **SQLite**, and **Google Gemini API**. The assistant helps students, faculty, and visitors quickly access campus information through natural language conversations.

---

## 📌 Features

- 🤖 AI-powered chatbot using Google Gemini
- 📚 Answer questions about campus facilities
- 🗓️ Class schedule assistance
- 👨‍🏫 Faculty information lookup
- 🏫 Department information
- 📍 Campus navigation support
- 📝 Event information
- 💾 SQLite database integration
- 🎨 Simple Streamlit web interface

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web Interface |
| SQLite | Database |
| Google Gemini API | AI Model |
| dotenv | Environment Variable Management |

---

## 📂 Project Structure

```
smart_campus_management/
│
├── main.py                 # Streamlit application
├── agent.py                # AI Agent logic
├── llm.py                  # Gemini API integration
├── database.py             # Database operations
├── campus.db               # SQLite database
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-campus-ai-agent.git

cd smart-campus-ai-agent
```

---

### 2. Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` File

Create a file named

```
.env
```

Add your Gemini API Key

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

### 5. Run the Project

```bash
streamlit run main.py
```

The application will open in your browser.

---

## 💬 Example Questions

- Where is the Computer Science department?
- Show today's events.
- Who is the HOD of IT?
- What are the library timings?
- Where is the admission office?
- Tell me about campus facilities.
- What is today's class schedule?

---

## 📸 Application Preview

(Add screenshots here)

Example:

```
Home Screen

Chat Interface

AI Response
```

---

## 🔮 Future Improvements

- Voice Assistant
- Student Login
- Faculty Login
- Attendance Tracking
- Hostel Management
- Fee Payment Assistant
- Campus Map Integration
- PDF Document Search (RAG)
- Multi-language Support
- Email Notifications

---

## 📖 Learning Objectives

This project demonstrates:

- Prompt Engineering
- AI Agent Design
- LLM Integration
- API Handling
- Database Management
- Environment Variables
- Streamlit Development
- Python Programming

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---


B.Tech Information Technology Student

---

## ⭐ If you found this project helpful, please give it a Star!
