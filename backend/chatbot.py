"""
chatbot.py

Handles communication with Gemini.
Returns JSON instead of plain text.
"""

import json

from .config import get_gemini_client
from .prompts import SHOPPING_SYSTEM_PROMPT

client = get_gemini_client()


def generate_response(user_input: str):

    prompt = f"""
{SHOPPING_SYSTEM_PROMPT}

Products:

{user_input}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        # Remove markdown if Gemini adds it
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        # Convert JSON string -> Python Dictionary
        return json.loads(text)

    except Exception as e:

        return {
            "best_overall": {
                "platform": "",
                "product": "",
                "reason": f"Gemini Error: {e}"
            },

            "best_budget": {
                "platform": "",
                "product": "",
                "reason": ""
            },

            "best_rated": {
                "platform": "",
                "product": "",
                "reason": ""
            },

            "final_recommendation": "Unable to generate recommendation."
        }

        