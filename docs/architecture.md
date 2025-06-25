# System Architecture: Mental Health Chatbot

## Overview
This chatbot tracks user emotions and responds empathetically. Data is stored in JSON files for session continuity.

## Modules

### 1. `chatbot.ipynb`
Main loop, integrates:
- User input/output
- Emotion recognition
- File utilities
- Summary generation

### 2. `utils/`
- `file_utils.py`: Handles file I/O
- `summarizer.py`: Creates summaries using Gemini

### 3. `data/`
- `summaries/`: Stores conversation summaries per user
- `histories/`: Stores chat logs per user

## Workflow
1. User starts a chat
2. Responses and emotions are logged
3. When chat ends, a summary is generated using Gemini
4. User can delete or modify stored data on request

## Notes
- Gemini API is used for content generation
- NLTK is used for tokenization and stopword removal
