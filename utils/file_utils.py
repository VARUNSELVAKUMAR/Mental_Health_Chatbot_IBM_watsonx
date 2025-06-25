import os
import json

def get_history_file(user_name):
    return f"data/histories/{user_name}_chat_history.json"

def get_summary_file(user_name):
    return f"data/summaries/{user_name}_chat_summary.json"

def load_json_file(path, default):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return default

def save_json_file(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_chat_history(user_name):
    return load_json_file(get_history_file(user_name), {"user_info": {}, "chat_history": []})

def save_chat_history(user_name, history):
    save_json_file(get_history_file(user_name), history)

def load_chat_summary(user_name):
    return load_json_file(get_summary_file(user_name), [])

def save_chat_summary(user_name, summary):
    summaries = load_chat_summary(user_name)
    summaries.append(summary)
    save_json_file(get_summary_file(user_name), summaries)
