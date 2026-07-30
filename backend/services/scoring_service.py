"""
scoring_service.py

Unified product scoring engine providing normalized 0-100 performance scores
based on price competitiveness, user star ratings, review volume, delivery speed, and active offers.
"""

from typing import List, Dict, Any


def calculate_product_score(product: Dict[str, Any], avg_price_in_set: float = 0.0) -> float:
    """
    Calculates a normalized score (0.0 to 100.0) for a product item.

    Components:
    - Rating Score (0-35 points)
    - Review Volume Score (0-15 points)
    - Price Value Score (0-35 points)
    - Delivery & Offers Bonus (0-15 points)
    """
    score = 0.0

    # 1. Rating Score (Max 35 points)
    rating = float(product.get("rating", 0.0))
    rating_score = (min(max(rating, 0.0), 5.0) / 5.0) * 35.0
    score += rating_score

    # 2. Review Volume Score (Max 15 points)
    reviews_count = int(product.get("reviews", product.get("reviews_count", 0)))
    review_score = min(15.0, (reviews_count / 1000.0) * 3.0)
    score += review_score

    # 3. Price Value Score (Max 35 points)
    price = float(product.get("price", 0.0))
    if avg_price_in_set > 0 and price > 0:
        price_ratio = price / avg_price_in_set
        if price_ratio <= 1.0:
            # Cheaper than average: 25 to 35 points
            price_score = 25.0 + (1.0 - price_ratio) * 10.0
        else:
            # More expensive than average: scale down from 25 to min 5
            price_score = max(5.0, 25.0 - (price_ratio - 1.0) * 15.0)
    else:
        price_score = 20.0
    score += price_score

    # 4. Delivery & Offers Bonus (Max 15 points)
    delivery_str = str(product.get("delivery", product.get("delivery_info", ""))).lower()
    if "tomorrow" in delivery_str or "1 day" in delivery_str or "express" in delivery_str:
        score += 10.0
    elif "2 days" in delivery_str or "2 day" in delivery_str:
        score += 6.0
    else:
        score += 3.0

    offers_str = str(product.get("offers", "")).lower()
    if offers_str and offers_str != "no offers" and offers_str != "no offers available":
        score += 5.0

    return round(min(100.0, score), 2)


def score_and_rank_products(products: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Scores every product in the list using relative category averages and returns
    sorted list (highest score first).
    """
    if not products:
        return []

    # Calculate average price across products
    prices = [float(p.get("price", 0.0)) for p in products if float(p.get("price", 0.0)) > 0]
    avg_price = sum(prices) / len(prices) if prices else 0.0

    ranked_products = []
    for p in products:
        p_copy = dict(p)
        p_copy["score"] = calculate_product_score(p_copy, avg_price_in_set=avg_price)
        ranked_products.append(p_copy)

    # Sort descending by score
    ranked_products.sort(key=lambda item: item["score"], reverse=True)
    return ranked_products
