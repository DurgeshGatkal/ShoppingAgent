Earlier our UI was not connected to gemini means it was not responding to user inputs
So, now we are going to connect the UI to Gemini(Fronted Backend Connection).

🎯 Goal:
User

↓

Streamlit UI

↓

Gemini API

↓

AI Response

↓

Streamlit UI

After today, your web app will actually answer questions using Gemini instead of returning a placeholder.


Until now:
User

↓

Streamlit

↓

"This will later come from Gemini."

Today:
User

↓

Streamlit

↓

Gemini API

↓

Shopping Assistant Response

# steps we  are perfroming  to connect fronted - backend

# Step 2 – Reuse Existing Backend
Remember this function in config.py?
get_gemini_client()

Excellent.

We're going to reuse it.

This is why we separated configuration on Day 1.


# Step 3 – Edit frontend/app.py
Find this line
ai_response = "🤖 This will later come from Gemini."

Replace it with
from backend.config import get_gemini_client
from backend.prompts import SHOPPING_SYSTEM_PROMPT

client = get_gemini_client()

full_prompt = f"""
{SHOPPING_SYSTEM_PROMPT}

User Question:

{user_prompt}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=full_prompt
)

ai_response = response.text


# Step 4 – Import Backend
At the top of frontend/app.py

Find
import streamlit as st


Replace with
import streamlit as st

import sys
from pathlib import Path

# Add backend folder to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from backend.config import get_gemini_client
from backend.prompts import SHOPPING_SYSTEM_PROMPT

 
 Why?
Your project has two folders:

frontend/
backend/

Python doesn't automatically know where backend is.

These lines tell Python where to find it.


# Step 5 – Add Error Handling
Replace

response = client.models.generate_content(...)

with 
try:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    ai_response = response.text

except Exception as e:

    ai_response = f"❌ Error: {e}"


Professional applications should never crash because of one API error.
💡 Why Are We Using try-except?

Imagine this situation:

Your internet disconnects.
Your API key is invalid.
Gemini servers are temporarily unavailable.

Without try-except:

❌ Your Streamlit app crashes.

With try-except:

✅ The app stays running and shows a friendly error message like:

❌ Error: API key is invalid.

This is much more professional.


🎯 Test It:
Ask:

Suggest a gaming laptop under ₹80,000.

Ask:

Which phone is best under ₹30,000?

Ask:

OLED vs LCD


🧠 What You Learned Today:
| Concept                          | Why it matters                                        |
| -------------------------------- | ----------------------------------------------------- |
| Reusing backend functions        | Avoids duplicate code and keeps the project organized |
| Importing modules across folders | Lets the frontend use backend logic                   |
| Calling Gemini from Streamlit    | Connects the user interface to the AI model           |
| Error handling                   | Prevents crashes when something goes wrong            |
