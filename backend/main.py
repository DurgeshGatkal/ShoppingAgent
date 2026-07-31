"""
main.py

FastAPI REST API application server for BuySense AI.
Provides REST endpoints for product search, AI scoring & recommendations, and conversational chat.
"""

from typing import List, Dict, Any, Optional
from fastapi import FastAPI, Depends, Query, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from backend.config import get_settings
from backend.database.connection import get_db
from backend.services.search import search_products
from backend.ai.recommendation_engine import generate_recommendation
from backend.services.ai_service import generate_ai_recommendation
from backend.config import get_gemini_client

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="REST API powering product search, AI scoring engine, structured recommendations, and shopping chatbot.",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Request & Response Schemas ---

class RecommendRequest(BaseModel):
    query: Optional[str] = Field(None, description="Search query string")
    products: Optional[List[Dict[str, Any]]] = Field(None, description="List of products to compare")


class ChatRequest(BaseModel):
    message: str = Field(..., description="User message or follow-up question")
    context_products: Optional[List[Dict[str, Any]]] = Field(None, description="Optional products context")


class HealthResponse(BaseModel):
    status: str
    app_name: str
    environment: str


# --- API Endpoints ---

@app.get("/", tags=["General"])
def root():
    """API Welcome root endpoint."""
    return {
        "message": f"Welcome to {settings.app_name} API",
        "docs": "/docs",
        "health": "/api/v1/health"
    }


@app.get("/api/v1/health", response_model=HealthResponse, tags=["General"])
def health_check():
    """Health check endpoint confirming API status."""
    return {
        "status": "online",
        "app_name": settings.app_name,
        "environment": settings.environment
    }


@app.get("/api/v1/products/search", tags=["Products"])
def search_products_endpoint(
    query: str = Query("", description="Search term (e.g. 'iphone', 'laptop')"),
    db: Session = Depends(get_db)
):
    """
    Search product catalog from SQLite database matching query term.
    """
    try:
        results = search_products(query, db=db)
        return {
            "count": len(results),
            "query": query,
            "products": results
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database search failed: {str(e)}"
        )


@app.post("/api/v1/recommend", tags=["AI Recommendation"])
def get_recommendations_endpoint(
    payload: RecommendRequest,
    db: Session = Depends(get_db)
):
    """
    Scores products and generates structured AI recommendation using Gemini.
    Accepts either an explicit product list or a search query string.
    """
    try:
        products = payload.products
        if not products and payload.query:
            products = search_products(payload.query, db=db)
        elif not products:
            products = search_products("", db=db)

        recommendation_result = generate_recommendation(products)
        return recommendation_result

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Recommendation engine error: {str(e)}"
        )


@app.post("/api/v1/chat", tags=["AI Chatbot"])
def chat_assistant_endpoint(payload: ChatRequest):
    """
    Interactive shopping assistant chatbot endpoint answering follow-up queries.
    """
    try:
        client = get_gemini_client()

        context_str = ""
        if payload.context_products:
            context_str = "\nCurrently Viewed Products:\n"
            for p in payload.context_products[:5]:
                context_str += f"- {p.get('name')} on {p.get('platform')} (Price: ₹{p.get('price')}, Rating: {p.get('rating')})\n"

        prompt = f"""
You are BuySense AI, an expert, objective shopping decision assistant.
Answer the user's question concisely, highlighting key product specifications, pros/cons, and price value.

{context_str}

User Question: {payload.message}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {
            "user_message": payload.message,
            "reply": response.text.strip()
        }

    except Exception as e:
        return {
            "user_message": payload.message,
            "reply": f"Shopping Assistant Note: Unable to reach Gemini AI ({e}). Please ensure your GEMINI_API_KEY is configured."
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
