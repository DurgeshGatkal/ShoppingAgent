"""
index_vectors.py

Script to load all products from the SQLite database and index them
into ChromaDB using Gemini text embeddings.

Run once after seeding the database:
    python -m backend.database.index_vectors
"""

from backend.database.connection import SessionLocal
from backend.services.search import search_products
from backend.services.vector_service import index_products, get_indexed_count


def main():
    print("=" * 55)
    print("  BuySense AI - Vector Index Builder")
    print("=" * 55)

    db = SessionLocal()
    try:
        print("\nLoading all products from SQLite database...")
        products = search_products(query="", db=db)
        print(f"Found {len(products)} products in database.")

        if not products:
            print("No products in database. Run seed.py first:\n  python -m backend.database.seed")
            return

        print()
        indexed = index_products(products)

        total = get_indexed_count()
        print(f"\nVector index ready: {total} total products indexed in ChromaDB.")
        print("Semantic search is now enabled!")
        print("=" * 55)

    except Exception as e:
        print(f"\nIndexing Error: {e}")
        print("Ensure your GEMINI_API_KEY is set in your .env file.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
