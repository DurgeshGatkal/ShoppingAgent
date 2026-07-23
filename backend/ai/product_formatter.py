"""
Converts product data into a clean format
that can be sent to Gemini.
"""

def format_products(products):

    formatted = ""

    for index, product in enumerate(products, start=1):

        formatted += f"""
Product {index}

Name: {product['name']}
Platform: {product['platform']}
Price: ₹{product['price']}
Rating: {product['rating']}
Reviews: {product['reviews']}
Delivery: {product['delivery']}
Offers: {product['offers']}

----------------------------------
"""

    return formatted

    