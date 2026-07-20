from backend.services.search import search_products

results = search_products("iphone")

for product in results:
    print(product)
    