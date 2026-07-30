"""
config.py

Manages application settings and environment variables using Pydantic Settings.
Configures and initializes the Google Gemini API client.
"""

import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
from google import genai
from pydantic_settings import BaseSettings


# Resolve project root and backend directory paths
BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = Path(__file__).resolve().parent

# Load environment variables from root .env or backend/.env
if (BASE_DIR / ".env").exists():
    load_dotenv(BASE_DIR / ".env")
elif (BACKEND_DIR / ".env").exists():
    load_dotenv(BACKEND_DIR / ".env")
else:
    load_dotenv()


class Settings(BaseSettings):
    """Application settings schema validating environment variables."""
    app_name: str = "BuySense AI"
    environment: str = "development"
    debug: bool = True
    api_port: int = 8000
    gemini_api_key: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


def get_settings() -> Settings:
    """Returns validated application settings instance."""
    return Settings(
        gemini_api_key=os.getenv("GEMINI_API_KEY")
    )


def get_gemini_client() -> genai.Client:
    """
    Creates and returns a Gemini client instance.

    Returns:
        genai.Client: Configured Gemini client
    """
    settings = get_settings()
    api_key = settings.gemini_api_key or os.getenv("GEMINI_API_KEY")

    if not api_key or api_key == "your_gemini_api_key_here":
        raise ValueError(
            "GEMINI_API_KEY not set. Please copy .env.example to .env and set a valid GEMINI_API_KEY."
        )

    return genai.Client(api_key=api_key)