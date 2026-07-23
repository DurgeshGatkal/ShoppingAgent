"""
Ranks products before sending them to Gemini.

Current ranking:
Higher rating
Lower price

Later we will add:

Delivery
Offers
Seller Rating
Warranty
"""

def rank_products(products):

    ranked = sorted(
        products,
        key=lambda product: (
            -product["rating"],
            product["price"]
        )
    )

    return ranked

    