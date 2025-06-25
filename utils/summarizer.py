import time
import google.generativeai as genai
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from .file_utils import *

def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    return " ".join([w for w in words if w.lower() not in stop_words])

def generate_summary(user_name):
    chat_history = load_chat_history(user_name)
    conversation_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    model = genai.GenerativeModel("gemini-2.0-flash-lite")

    response = model.generate_content(f"""Summarize this user's conversation:
    {chat_history}

    Include emotional highlights, key topics, and the timestamp {conversation_time}.
    """)

    summary_text = remove_stopwords(response.text.strip())
    save_chat_summary(user_name, {
        "conversation_time": conversation_time,
        "summary": summary_text
    })

    # Clear history file after summary
    save_chat_history(user_name, {"user_info": {}, "chat_history": []})
