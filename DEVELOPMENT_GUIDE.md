# BuySense AI — Development & Execution Guide

This document is your living tracker for the entire BuySense AI rebuild. It details all technical changes completed by the AI Assistant in each phase, along with specific **action items for you (the developer)**.

---

## 🚨 IMPORTANT SECURITY FIX (API Key & Git Push Issues)

### Why GitHub Blocked Your Push:
GitHub has automated secret scanners. A real Google Gemini API Key was accidentally pasted into `.env.example`. Since `.env.example` is tracked by Git, GitHub detected the secret key and blocked your push to protect your account.

### How We Fixed It:
1. **Cleaned `.env.example`**: Replaced the real key with the dummy placeholder `GEMINI_API_KEY=your_gemini_api_key_here`.
2. **Updated `.gitignore`**: Ensured `.env`, `*.env`, `database/*.db`, and cache folders are strictly ignored so secrets and binary database files never get pushed to GitHub.

---

## 📌 Phase 1: Environment & Dependency Setup (COMPLETED ✅)

### 🛠️ Changes Completed by AI:
1. **Created `requirements.txt`**: Added production dependencies for FastAPI, Uvicorn, Streamlit, Gemini SDK (`google-genai`), SQLAlchemy, ChromaDB, Pydantic, and Pytest.
2. **Created `.env.example`**: Standardized environment variable template for secret management.
3. **Upgraded `backend/config.py`**: Integrated Pydantic `BaseSettings` for robust environment variable validation and safe Gemini client initialization.
4. **Cleaned Up Dead Code**: Permanently removed unused duplicate files `backend/ai/ranker.py` and `backend/ai/ranking.py`.

---

## 📌 Phase 2: Database Layer & Data Models (COMPLETED ✅)

### 🛠️ Changes Completed by AI:
1. **Created `backend/database/connection.py`**: Configured SQLite database connection (`database/buysense.db`) using SQLAlchemy ORM engine.
2. **Created `backend/database/models.py`**: Built relational database tables (`Platform`, `Product`, `Specification`).
3. **Created `backend/schemas/product_schema.py`**: Built Pydantic models (`ProductCreate`, `ProductResponse`, `SpecificationSchema`) for API validation.
4. **Created & Ran `backend/database/seed.py`**: Created SQLite database tables and seeded 8+ rich e-commerce products with hardware specifications.
5. **Updated `backend/services/search.py`**: Replaced static list filtering with fast case-insensitive SQL queries (`Product.name.ilike()`, `Product.brand.ilike()`).

---

## 📌 Phase 3: Core AI & Scoring Engine (COMPLETED ✅)

### 🛠️ Changes Completed by AI:
1. **Created `backend/services/scoring_service.py`**:
   - Replaced legacy math formulas with a normalized 0–100 weighted product scoring algorithm.
   - Evaluates: User Ratings (35%), Review Volume (15%), Price Value relative to category average (35%), and Delivery Speed & Offers (15%).
2. **Created `backend/services/ai_service.py`**:
   - Assembles full hardware specifications (Storage, RAM, Display, Processor, Camera, Battery) into structured LLM prompts.
   - Configures Gemini 2.5 Flash using native JSON response mode (`response_mime_type="application/json"`).
   - Added robust fallback error handling so the app never crashes if the API encounters rate limits.
3. **Refactored `backend/ai/recommendation_engine.py`**:
   - Streamlined pipeline to orchestrate `scoring_service.py` and `ai_service.py`.

### 👤 Action Items for You (Durgesh):
- [ ] **Run Test Script**: Run `python test_recommendation.py` in your terminal to test product scoring and AI recommendation output.

---

## 💡 Recommended Features & Future Roadmap (Post-Phase 3)

Below are high-impact feature recommendations, architectural improvements, and the step-by-step roadmap for the upcoming phases to transform BuySense AI into an industry-grade shopping decision agent.

---

### 🌟 1. Key Features & Ideas to Improve the Project

#### Feature 1: Interactive Price Trend & Historical Charts 📈
- **Concept**: Display a 30-day, 60-day, or 90-day price history graph (using Plotly/Altair in Streamlit) for selected products.
- **Value**: Users can instantly see if current prices are at an all-time low or if they should wait for an upcoming festival sale.

#### Feature 2: Multi-Agent AI System (Specialized Shopping Agents) 🤖
- Instead of a single LLM prompt, split the AI into specialized micro-agents:
  - **Deal Finder Agent**: Scans for active bank discounts, exchange bonuses, and coupon codes.
  - **Review Summarizer Agent**: Analyzes customer reviews to highlight pros and cons (e.g. *"Great camera, but battery drains fast during gaming"*).
  - **Hardware Spec Agent**: Compares technical benchmarks (Geekbench processor scores, display refresh rate, camera MP).
  - **Supervisor Agent**: Synthesizes agent findings into the final purchase decision guide.

#### Feature 3: Conversational AI Shopping Assistant (Multi-Turn Chat) 💬
- **Concept**: Add a dedicated interactive chat tab where users can ask follow-up questions after viewing recommendations.
- **Example Queries**:
  - *"Why is Amazon better than Flipkart for the iPhone 16?"*
  - *"Which of these phones has the best low-light camera performance?"*
  - *"Recommend a phone under ₹50,000 for vlogging with fast charging."*

#### Feature 4: Semantic Vector Search & RAG (ChromaDB Integration) 🔍
- **Concept**: Enable natural language intent search using vector embeddings instead of exact keyword matching.
- **Value**: Handles queries like *"wireless earbuds with deep bass and long battery under 3k"* even if those exact words aren't in the product title.

#### Feature 5: Price Drop Alerts & User Wishlist 🔔
- Allow users to bookmark favorite products and receive email/SMS notifications when prices drop below a target threshold.

---

### 🗺️ Next Steps Roadmap (Phases 4 → 5 → 6)

```
[Phase 4: FastAPI REST API Server] ──► [Phase 5: Vector DB RAG Engine] ──► [Phase 6: Modern UI & Chatbot]
```

#### 📌 Phase 4: FastAPI Backend REST API Server (NEXT PHASE ⏳)
- Create `backend/main.py` using FastAPI.
- Build clean, decoupled REST endpoints:
  - `GET /api/v1/products/search?query=iphone`
  - `POST /api/v1/recommend`
  - `POST /api/v1/chat`
- Add Swagger API documentation (`http://localhost:8000/docs`).

#### 📌 Phase 5: Vector DB (ChromaDB) & RAG Integration
- Initialize ChromaDB vector database.
- Embed product descriptions and review text for semantic hybrid search.

#### 📌 Phase 6: Streamlit Frontend Redesign & Conversational AI Chatbot UI
- Connect Streamlit UI to FastAPI REST endpoints using `requests`.
- Add interactive multi-turn chat widget (`st.chat_message`, `st.chat_input`).
- Fix quick-search popular buttons and polish CSS layout.

---
*Guide compiled & updated by Antigravity AI*
