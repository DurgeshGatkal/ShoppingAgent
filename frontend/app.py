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
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================
# Sidebar
# ===========================

with st.sidebar:

    st.title("🛍️ BuySense AI")

    st.markdown("---")

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.subheader("📂 Recent Chats")

    st.caption("Laptop under ₹60,000")
    st.caption("Best Gaming Phone")
    st.caption("Wireless Earbuds")

    st.markdown("---")

    st.subheader("⚙ Settings")

    st.write("Version : 1.0")



# -----------------------------
# Title and Subtitle
# -----------------------------
st.title("🛍️ BuySense AI")

st.caption("AI Shopping Decision Assistant")

st.markdown(
    """
### Find the Best Product with AI

Compare products, analyze reviews,
and make smarter shopping decisions.
"""
)


st.subheader("💡 Try asking")

col1, col2 = st.columns(2)

with col1:
    st.info("💻 Best Laptop under ₹60,000")
    st.info("🎧 Best Earbuds under ₹3,000")

with col2:
    st.info("📱 Compare iPhone vs Samsung")
    st.info("⌚ Best Smartwatch under ₹5,000")

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
user_prompt = st.chat_input(
    "Ask about laptops, mobiles, TVs, headphones..."
)


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

    

with st.spinner("🤖 BuySense AI is thinking..."):
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


        