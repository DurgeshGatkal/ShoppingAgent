from backend.services.search import search_products
from backend.ai.recommendation_engine import generate_recommendation

products = search_products("iphone")

result = generate_recommendation(products)

print("\n========== RANKED PRODUCTS ==========\n")

for product in result["ranked_products"]:

    print(product["platform"])
    print(product["price"])
    print(product["rating"])
    print(product["score"])
    print("--------------------------")

print("\n========== AI RECOMMENDATION ==========\n")

print(result["recommendation"])

