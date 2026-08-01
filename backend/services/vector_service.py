"""
vector_service.py

ChromaDB Vector Store integration for BuySense AI.
Handles product embedding generation using Gemini Embeddings API and semantic similarity search.
"""

import os
from pathlib import Path
from typing import List, Dict, Any, Optional
import chromadb
from chromadb.config import Settings as ChromaSettings


# ChromaDB persistent storage folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CHROMA_DIR = str(BASE_DIR / "chroma_db")

COLLECTION_NAME = "buysense_products"


def get_chroma_client() -> chromadb.PersistentClient:
    """Returns persistent ChromaDB client."""
    return chromadb.PersistentClient(
        path=CHROMA_DIR,
        settings=ChromaSettings(anonymized_telemetry=False)
    )


def get_collection() -> chromadb.Collection:
    """Returns (or creates) the BuySense products collection."""
    client = get_chroma_client()
    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )


def _build_product_text(product: Dict[str, Any]) -> str:
    """
    Builds a structured text representation of a product for embedding.
    Includes all searchable fields: name, brand, category, specs, and description.
    """
    return (
        f"{product.get('name', '')} by {product.get('brand', '')}. "
        f"Category: {product.get('category', '')}. "
        f"Platform: {product.get('platform', '')}. "
        f"Price: {product.get('price', '')}. "
        f"Processor: {product.get('processor', '-')}. "
        f"RAM: {product.get('ram', '-')}. Storage: {product.get('storage', '-')}. "
        f"Display: {product.get('display', '-')}. "
        f"Camera: {product.get('camera', '-')}. Battery: {product.get('battery', '-')}. "
        f"Delivery: {product.get('delivery', product.get('delivery_info', '-'))}. "
        f"Offers: {product.get('offers', '-')}. "
        f"Description: {product.get('description', '')}."
    )


def get_embeddings_from_gemini(texts: List[str]) -> List[List[float]]:
    """
    Generates text embeddings using Gemini embedding model.
    """
    from backend.config import get_gemini_client
    client = get_gemini_client()
    embeddings = []
    for text in texts:
        response = client.models.embed_content(
            model="models/gemini-embedding-001",
            contents=text,
        )
        embeddings.append(response.embeddings[0].values)
    return embeddings


def index_products(products: List[Dict[str, Any]]) -> int:
    """
    Indexes product list into ChromaDB with Gemini embeddings.
    Skips products that are already indexed.

    Returns:
        int: Number of newly indexed products
    """
    if not products:
        return 0

    collection = get_collection()
    existing_ids = set(collection.get()["ids"])

    new_products = [p for p in products if str(p["id"]) not in existing_ids]
    if not new_products:
        print(f"All {len(products)} products already indexed.")
        return 0

    texts = [_build_product_text(p) for p in new_products]
    ids = [str(p["id"]) for p in new_products]
    metadatas = [
        {
            "name": str(p.get("name", "")),
            "brand": str(p.get("brand", "")),
            "platform": str(p.get("platform", "")),
            "price": str(p.get("price", 0)),
            "category": str(p.get("category", "")),
        }
        for p in new_products
    ]

    print(f"Generating Gemini embeddings for {len(new_products)} products...")
    embeddings = get_embeddings_from_gemini(texts)

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )
    print(f"Successfully indexed {len(new_products)} products into ChromaDB.")
    return len(new_products)


def semantic_search(query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    """
    Performs semantic similarity search across indexed products using a text query.

    Args:
        query (str): Natural language search query.
        top_k (int): Maximum number of results to return.

    Returns:
        List[Dict]: Matching product metadata and similarity scores.
    """
    collection = get_collection()
    count = collection.count()

    if count == 0:
        return []

    # Embed the user query
    query_embedding = get_embeddings_from_gemini([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(top_k, count),
        include=["documents", "metadatas", "distances"]
    )

    output = []
    for i, meta in enumerate(results["metadatas"][0]):
        similarity = round(1.0 - results["distances"][0][i], 4)
        output.append({
            **meta,
            "similarity_score": similarity,
            "document_snippet": results["documents"][0][i][:200]
        })

    return output


def get_indexed_count() -> int:
    """Returns total number of currently indexed products."""
    return get_collection().count()
