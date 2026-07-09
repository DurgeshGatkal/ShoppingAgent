"""
config.py

This file is responsible for:
1. Loading environment variables.
2. Creating the Gemini client.
3. Returning the client to other files.
"""

from dotenv import load_dotenv
from google import genai
import os


# Load variables from .env file
load_dotenv()


def get_gemini_client():
    """
    Creates and returns a Gemini client.

    Returns:
        genai.Client: Configured Gemini client
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file.")

    client = genai.Client(api_key=api_key)

    return client