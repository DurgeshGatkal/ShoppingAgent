"""
BuySense AI - Streamlit Frontend

This is the frontend for our AI Shopping Decision Agent.
Currently, it only displays a chat interface.
Gemini integration will be added in the next step.
"""

import streamlit as st

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from backend.chatbot import generate_response

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="BuySense AI",
    page_icon="🛍️",
    layout="centered"
)

# -----------------------------
# Title and Subtitle
# -----------------------------
st.title("🛍️ BuySense AI")
st.subheader("AI Shopping Decision Assistant")

st.write(
    "Welcome! I can help you compare products, recommend the best options, "
    "and make smarter shopping decisions."
)

st.divider()

# -----------------------------
# Initialize Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Previous Messages
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
user_prompt = st.chat_input("Ask me about any product...")

if user_prompt:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    

   # Get response from backend
ai_response = generate_response(user_prompt)

    # Store AI response
st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )

    # Display AI response
with st.chat_message("assistant"):
        st.markdown(ai_response)