def calculate_score(features):

    score = 0

    # Lower price = higher score
    score += (100000 - features["price"]) / 1000

    # Rating score
    score += features["rating"] * 10

    return round(score, 2)

    