"""
search.py

Product search service querying the SQLite database via SQLAlchemy ORM.
"""

from typing import List, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import or_
from backend.database.connection import SessionLocal
from backend.database.models import Product, Specification


def search_products(query: str, db: Session = None) -> List[Dict[str, Any]]:
    """
    Searches products from SQLite database matching query against name, brand, or category.

    Args:
        query (str): Search string keyword
        db (Session, optional): SQLAlchemy DB session

    Returns:
        List[Dict[str, Any]]: List of dictionary products matching query
    """
    close_session = False
    if db is None:
        db = SessionLocal()
        close_session = True

    try:
        if not query or not query.strip():
            products = db.query(Product).all()
        else:
            q = f"%{query.strip().lower()}%"
            products = db.query(Product).filter(
                or_(
                    Product.name.ilike(q),
                    Product.brand.ilike(q),
                    Product.category.ilike(q)
                )
            ).all()

        results = []
        for p in products:
            p_dict = {
                "id": p.id,
                "name": p.name,
                "brand": p.brand,
                "platform": p.platform,
                "price": p.price,
                "rating": p.rating,
                "reviews": p.reviews_count,
                "category": p.category,
                "image": p.image_url or "https://via.placeholder.com/200",
                "delivery": p.delivery_info,
                "offers": p.offers,
                "description": p.description,
                "url": p.url,
            }

            if p.specification:
                p_dict.update({
                    "storage": p.specification.storage,
                    "ram": p.specification.ram,
                    "display": p.specification.display,
                    "processor": p.specification.processor,
                    "camera": p.specification.camera,
                    "battery": p.specification.battery,
                    "color": p.specification.color,
                })
            else:
                p_dict.update({
                    "storage": "-", "ram": "-", "display": "-",
                    "processor": "-", "camera": "-", "battery": "-", "color": "-"
                })

            results.append(p_dict)

        return results

    finally:
        if close_session:
            db.close()