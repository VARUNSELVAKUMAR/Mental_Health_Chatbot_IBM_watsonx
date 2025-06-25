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


## 📦 Installation

1. Clone the repo:
   ```
   git clone https://github.com/VARUNSELVAKUMAR/Mental_Health_Chatbot_IBM_watsonx.git<br>
   cd Mental_Health_Chatbot_IBM_watsonx

3. Install Requirements:
   ```
   pip install -r requirements.txt

5. Ensure nltk resources:
   ```
   import nltk
   nltk.download("punkt")
   nltk.download("stopwords")

7. Set your Gemini API Key inside chatbot.py:
   ```
   genai.configure(api_key="YOUR_API_KEY")
<i>  Note: To get your Gemini API key, you can use Gemini AI studio. Check this https://ai.google.dev/gemini-api/docs/api-key for more information.</i>
<br>
* You can check the JSON files of a sample chat conversation to understand how the JSON files are getting updated.
* Additionally you can refer the project report for additional details.

<b>Important Feature:</b> Based on the username, different profiles are created and when the user returns, their respective previous conversation summary is retrieved.


## 💡 Usage

Run the chatbot.py notebook to:

   * Start the chatbot interaction loop.

   * Handle user inputs, emotions, summaries.

   * Maintain user memory unless cleared.

## 🔐 Privacy & Ethics

   * No external database or tracking.

   * Users can erase their data.

   * No medical advice or medication is provided.





