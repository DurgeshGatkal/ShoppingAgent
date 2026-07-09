Objective
The objective of Day 1 is to establish communication between the BuySense AI application and Google's Gemini model. At this stage, the application behaves as a simple terminal-based chatbot capable of accepting user input and generating AI responses.


Why do we need an LLM?
A Large Language Model (LLM) is responsible for understanding natural language and generating meaningful responses. In BuySense AI, the LLM serves as the reasoning engine that will later compare products, summarize reviews, answer shopping-related questions, and provide recommendations.

Why Gemini?
Gemini was selected because:

Free API for students
Easy Python SDK
High-quality responses
Simple integration
Can later be replaced with another LLM


Components Used
python-dotenv

Purpose:
Load environment variables from a .env file.

Why?
To keep API keys outside the source code.


google-genai
Purpose:
Communicates with Google's Gemini API.


config.py
Purpose:
Creates and returns the Gemini client.

Benefits:
Cleaner code
Reusable
Easier maintenance


chatbot.py
Responsibilities:
Accept user input
Send prompt to Gemini
Display AI response
Continue until user exits


Current Architecture:
User

↓

chatbot.py

↓

config.py

↓

Gemini API

↓

AI Response


