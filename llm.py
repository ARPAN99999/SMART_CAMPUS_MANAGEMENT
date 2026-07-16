import os
import warnings

from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=FutureWarning, module="google.generativeai")

load_dotenv()

# Ensure the environment is available to Streamlit workers as well.
os.environ.setdefault("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY", ""))

try:
    import google.generativeai as genai
except ImportError:
    genai = None

api_key = os.getenv("GEMINI_API_KEY", "").strip()
model = None

if genai is not None and api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-flash-latest")


def ask_gemini(prompt):
    if model is None:
        return "Gemini API key is not configured. Set GEMINI_API_KEY in your environment or .env file to enable AI replies."

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as exc:
        return f"Sorry, I could not reach the Gemini API: {exc}"