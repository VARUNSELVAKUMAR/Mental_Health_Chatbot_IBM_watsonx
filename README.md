# Mental_Health_Chatbot_IBM_watsonx
AI-Powered Empathetic Mental Health Chatbot with Persistent Memory and Emotion Awareness using Gemini &amp; IBM watsonx.ai Studio
# 🧠 Mental Health Companion Chatbot

A compassionate, privacy-first mental health chatbot built with Google Gemini Pro and NLTK. Designed to engage with users in natural, emotionally sensitive conversations while maintaining summaries and chat histories in structured JSON format.

## ✨ Features

- 🧠 AI-powered empathetic conversations
- 🕒 Real-time emotional context with memory
- 📁 Local chat history and summary files (per user)
- 🧹 Clear specific or full memory upon user request
- 💬 Summarization of conversations at exit
- 📦 Gemini Pro integration for responses and summarization
- 🧹 Stopword removal to optimize summaries
- 🔁 Continuity between sessions via persistent summaries

## 🏗️ Architecture

chatbot.ipynb<br>
├── load/save history: utils/file_utils.py<br>
├── summarization logic: utils/summarizer.py<br>
├── mood/emotion checks: utils/emotion_tracker.py<br>
└── chat loop + Gemini integration<br>

## 📂 Folder Structure

mental-health-chatbot/<br>
├── utils/ # Utility scripts for file I/O, summaries<br>
├── data/ # Stores chat history and summary JSONs<br>
├── chatbot.ipynb # Main Jupyter Notebook with chat loop<br>
├── requirements.txt # Python packages needed<br>
├── README.md # Project overview<br>
└── docs/ # Architecture and contribution guide
