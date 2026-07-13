"""
chatbot.py

Contains the AI logic for BuySense AI.
The frontend will call the generate_response() function.
"""

from .config import get_gemini_client
from .prompts import SHOPPING_SYSTEM_PROMPT

# Create Gemini client only once
client = get_gemini_client()


def generate_response(user_input: str) -> str:
    """
    Generates an AI response for the given user query.

    Args:
        user_input (str): User's shopping-related question.

    Returns:
        str: AI-generated response.
    """

    full_prompt = f"""
{SHOPPING_SYSTEM_PROMPT}

User Question:
{user_input}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt
        )

        return response.text

    except Exception as e:

        return f"❌ Error: {e}"