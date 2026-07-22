from backend.ai.ranker import rank_products
from backend.config import get_gemini_client
from backend.prompts import SHOPPING_SYSTEM_PROMPT


def generate_recommendation(products):
    """
    Generates an AI recommendation for a list of products.

    Steps:
    1. Rank the products using our algorithm.
    2. Send the ranked products to Gemini.
    3. Return both the ranked products and AI response.
    """

    # -------------------------
    # Rank products
    # -------------------------
    ranked_products = rank_products(products)

    # -------------------------
    # Build Prompt
    # -------------------------
    comparison_data = ""

    for index, product in enumerate(ranked_products, start=1):

        comparison_data += f"""
Product {index}

Name: {product['name']}
Platform: {product['platform']}
Price: ₹{product['price']}
Rating: {product['rating']}
AI Score: {product['score']}

"""

    prompt = f"""
{SHOPPING_SYSTEM_PROMPT}

Below are the ranked shopping results.

{comparison_data}

Generate:

1. Best Overall Product
2. Best Budget Product
3. Pros and Cons of each product
4. Which product should the customer buy?
5. Explain your reasoning.
"""

    # -------------------------
    # Call Gemini
    # -------------------------
    client = get_gemini_client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "ranked_products": ranked_products,
        "recommendation": response.text
    }

    