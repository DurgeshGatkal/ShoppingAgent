from backend.services.search import search_products

results = search_products("samsung")

for product in results:
    print(product)
    
    