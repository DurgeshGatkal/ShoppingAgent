"""
recommendation_engine.py

Main recommendation pipeline orchestrating unified 0-100 product scoring and Gemini AI structured recommendation generation.
"""

from typing import List, Dict, Any
from backend.services.scoring_service import score_and_rank_products
from backend.services.ai_service import generate_ai_recommendation


def generate_recommendation(products: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Ranks products using relative scoring service and generates structured Gemini recommendation.

    Args:
        products (List[Dict]): List of product dictionaries.

    Returns:
        Dict: Contains 'ranked_products' (list) and 'recommendation' (dict).
    """
    if not products:
        return {
            "ranked_products": [],
            "recommendation": {
                "best_overall": {"platform": "", "product": "", "reason": "No matching products found."},
                "best_budget": {"platform": "", "product": "", "reason": ""},
                "best_rated": {"platform": "", "product": "", "reason": ""},
                "final_recommendation": "Search for products to receive AI recommendations."
            }
        }

    # 1. Score and rank products (0-100 normalized scale)
    ranked_products = score_and_rank_products(products)

    # 2. Pass ranked products with hardware specs to Gemini AI
    recommendation = generate_ai_recommendation(ranked_products)

    return {
        "ranked_products": ranked_products,
        "recommendation": recommendation
    }