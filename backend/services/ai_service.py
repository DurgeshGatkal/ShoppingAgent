"""
ai_service.py

AI Service managing Gemini LLM interaction, structured prompt assembly with complete hardware specifications,
and strict JSON response generation.
"""

import json
from typing import List, Dict, Any
from google.genai import types
from backend.config import get_gemini_client
from backend.prompts import SHOPPING_SYSTEM_PROMPT


def format_products_with_specs(products: List[Dict[str, Any]]) -> str:
    """
    Formats list of product dictionaries into structured text block including full hardware specifications.
    """
    formatted_text = ""
    for idx, p in enumerate(products, start=1):
        formatted_text += f"""
Product {idx}:
- Name: {p.get('name', 'N/A')}
- Brand: {p.get('brand', 'N/A')}
- Platform: {p.get('platform', 'N/A')}
- Price: ₹{p.get('price', 0):,}
- Rating: {p.get('rating', 0.0)} ({p.get('reviews', p.get('reviews_count', 0))} Reviews)
- Score: {p.get('score', 'N/A')}/100
- Delivery: {p.get('delivery', p.get('delivery_info', 'N/A'))}
- Offers: {p.get('offers', 'None')}
- Technical Specifications:
  * Storage: {p.get('storage', '-')}
  * RAM: {p.get('ram', '-')}
  * Display: {p.get('display', '-')}
  * Processor: {p.get('processor', '-')}
  * Camera: {p.get('camera', '-')}
  * Battery: {p.get('battery', '-')}
  * Color: {p.get('color', '-')}
- Description: {p.get('description', 'N/A')}
--------------------------------------------------
"""
    return formatted_text


def generate_ai_recommendation(products: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generates structured AI recommendations from Gemini using native JSON mode.

    Args:
        products (List[Dict]): List of product dictionaries with scores & specs.

    Returns:
        Dict: Structured recommendation containing best_overall, best_budget, best_rated, and final_recommendation.
    """
    if not products:
        return {
            "best_overall": {"platform": "", "product": "", "reason": "No products supplied for comparison."},
            "best_budget": {"platform": "", "product": "", "reason": ""},
            "best_rated": {"platform": "", "product": "", "reason": ""},
            "final_recommendation": "Search for products to get AI recommendations."
        }

    formatted_catalog = format_products_with_specs(products)
    prompt = f"{SHOPPING_SYSTEM_PROMPT}\n\nAvailable Products for Comparison:\n{formatted_catalog}"

    try:
        client = get_gemini_client()

        # Call Gemini using JSON response mime type configuration
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.2,
            )
        )

        text = response.text.strip()

        # Additional cleanups if any markdown backticks remain
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

        return json.loads(text)

    except Exception as e:
        print(f"Gemini API Recommendation Error: {e}")
        # Fallback dictionary if API fails or fails to parse
        return {
            "best_overall": {
                "platform": products[0].get("platform", ""),
                "product": products[0].get("name", ""),
                "reason": f"Top scored product. (Note: Gemini AI details temporarily unavailable: {e})"
            },
            "best_budget": {
                "platform": min(products, key=lambda x: x.get("price", 999999)).get("platform", ""),
                "product": min(products, key=lambda x: x.get("price", 999999)).get("name", ""),
                "reason": "Lowest price item in search results."
            },
            "best_rated": {
                "platform": max(products, key=lambda x: x.get("rating", 0)).get("platform", ""),
                "product": max(products, key=lambda x: x.get("rating", 0)).get("name", ""),
                "reason": "Highest rated item by user reviews."
            },
            "final_recommendation": f"Recommend considering {products[0].get('name')} on {products[0].get('platform')} based on overall product scoring."
        }
