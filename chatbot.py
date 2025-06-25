from utils.file_utils import load_chat_history, save_chat_history, load_chat_summary, save_chat_summary
from utils.summarizer import generate_summary
from utils.emotion_tracker import track_emotion, is_negative_streak

# Main loop
Latest_emotions = ["neutral", "neutral"]  # the latest emotions experienced by the user
n = 0

print("🤖 Chatbot: Hi! I’m here to listen. Please enter your name.")
user_name = input("👤 Enter your name: ")
print("🤖 Chatbot: How are you feeling today?")

while True:
    user_input = input("👤 You: ")
    emotion = input("Emotion: ")

    if (n == 0):
        Latest_emotions[n] = emotion
        n = 1
    else:
        Latest_emotions[n] = emotion
        n = 0

    if user_input.lower() in ["exit", "quit", "bye", "bubye", "talk to you later", "sayonara", " c u","cu", "see you", "ttyl", "okay bye", "cya", "see you later", "goodbye", "I am leaving", "I'm leaving"]:
        if (Latest_emotions.count("sad") == 2 or Latest_emotions.count("fear") == 2 or Latest_emotions.count("anger") == 2):
            print("🤖 Chatbot: Hope you are doing alright. If there's anything, I'm always here for you. Don't stress yourself. Things will get better\nTake care! Remember, you are not alone. 💙")
        else:
            print("🤖 Chatbot: Take care! Remember, you are not alone. 💙")

        # Generate the conversation summary and save it when conversation ends
        generate_conversation_summary(user_name)

        break

    response = mental_health_chatbot(user_name, user_input, emotion)
    if (response == 'CLEAR'):
      clear_data(user_name)
    else:
      print(f"🤖 Chatbot: {response}")
