# Day 5 - Project Architecture

## Objective

Refactor the project into a modular architecture by separating the frontend from the AI logic.

## Why?

A professional project should separate responsibilities.

Frontend:
- User Interface

Backend:
- AI Logic

Configuration:
- API Keys
- Gemini Client

Advantages:

- Easier maintenance
- Easier testing
- Easier to add new features
- Cleaner GitHub repository


# Changes done on Day 5.

Step 2

Moved AI logic into chatbot.py.

Before:
app.py

contained:
UI
Gemini
Prompt
API call

After:
app.py

contains only UI.


Step 3

Created generate_response()

Instead of writing Gemini code inside Streamlit:

response = client.models.generate_content(...)

we now simply call:

ai_response = generate_response(user_prompt)

This is called abstraction because the frontend does not need to know how the AI works internally.


