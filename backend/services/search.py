"""
Search Service

Responsible for searching products
from the product database.
"""

from backend.data.mock_products import PRODUCTS


def search_products(query: str):

    query = query.lower()

    results = []

    for product in PRODUCTS:

        if query in product["name"].lower():

            results.append(product)

    return results