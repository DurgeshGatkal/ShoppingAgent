from backend.ai.normalizer import normalize_product
from backend.ai.features import extract_features
from backend.ai.scoring import calculate_score


def rank_products(products):

    ranked = []

    for product in products:

        product = normalize_product(product)

        features = extract_features(product)

        score = calculate_score(features)

        product["score"] = score

        ranked.append(product)

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked

    