"""
recommendation_engine.py

Ranks products first.
Then asks Gemini to compare ALL platforms.
"""

from backend.chatbot import generate_response


# ----------------------------------
# Product Scoring Algorithm
# ----------------------------------

def calculate_score(product):

    score = 0

    # Higher rating = higher score
    score += product["rating"] * 15

    # Lower price = better
    score += max(0, 100000 - product["price"]) / 3000

    # Delivery

    if product["delivery"].lower() == "tomorrow":
        score += 10

    elif "2" in product["delivery"]:
        score += 5

    # Reviews

    score += min(product["reviews"] / 5000, 5)

    return round(score, 2)


# ----------------------------------
# Recommendation
# ----------------------------------

def generate_recommendation(products):

    if len(products) == 0:

        return {
            "ranked_products": [],
            "recommendation": None
        }

    # Score every product

    for product in products:

        product["score"] = calculate_score(product)

    # Highest score first

    ranked_products = sorted(
        products,
        key=lambda x: x["score"],
        reverse=True
    )

    # -----------------------------
    # Create prompt for Gemini
    # -----------------------------

    prompt = ""

    for product in ranked_products:

        prompt += f"""
Platform : {product['platform']}
Product : {product['name']}
Price : ₹{product['price']}
Rating : {product['rating']}
Reviews : {product['reviews']}
Delivery : {product['delivery']}
Score : {product['score']}

"""

    recommendation = generate_response(prompt)

    return {
        "ranked_products": ranked_products,
        "recommendation": recommendation
    }

    