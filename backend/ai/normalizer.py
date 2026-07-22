import re


def normalize_product(product):
    """
    Normalize product information.
    """

    normalized = product.copy()

    name = product["name"].lower()

    name = re.sub(r"\(.*?\)", "", name)

    name = name.replace("smartphone", "")

    name = " ".join(name.split())

    normalized["normalized_name"] = name

    return normalized

    