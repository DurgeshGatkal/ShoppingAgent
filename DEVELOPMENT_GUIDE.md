# BuySense AI — Development & Execution Guide

This document is your living tracker for the entire BuySense AI rebuild. It details all technical changes completed by the AI Assistant in each phase, along with specific **action items for you (the developer)**.

---

## 📌 Phase 1: Environment & Dependency Setup (COMPLETED ✅)

### 🛠️ Changes Completed by AI:
1. **Created `requirements.txt`**: Added production dependencies for FastAPI, Uvicorn, Streamlit, Gemini SDK (`google-genai`), SQLAlchemy, ChromaDB, Pydantic, and Pytest.
2. **Created `.env.example`**: Standardized environment variable template for secret management.
3. **Upgraded `backend/config.py`**: Integrated Pydantic `BaseSettings` for robust environment variable validation and safe Gemini client initialization.
4. **Cleaned Up Dead Code**: Permanently removed unused duplicate files `backend/ai/ranker.py` and `backend/ai/ranking.py`.

### 👤 Action Items for You (Durgesh):
- [ ] **Step 1**: In the project root directory (`c:\Users\Durgesh\Desktop\shopping agent`), create a new file named `.env` by copying `.env.example`.
- [ ] **Step 2**: Open your `.env` file and set your Gemini API key:
  ```env
  GEMINI_API_KEY=your_actual_gemini_api_key_here
  ```
  *(If you don't have a key, get a free one at [Google AI Studio](https://aistudio.google.com/app/apikey))*
- [ ] **Step 3**: (Optional) Open terminal and install updated dependencies:
  ```bash
  pip install -r requirements.txt
  ```

---

## 📌 Phase 2: Database Layer & Data Models (NEXT UP ⏳)

### 🎯 Objective:
Replace mock data with a real **SQLite Database** and **SQLAlchemy ORM** models for products, specifications, and platforms.

### 🛠️ Planned Changes:
1. Create `backend/database/models.py`: Define `Product`, `Specification`, and `Platform` database tables.
2. Create `backend/database/connection.py`: Set up SQLite database engine and session manager.
3. Create `backend/database/seed.py`: Seed script to populate 25+ real products with complete hardware specs.
4. Create `backend/schemas/product_schema.py`: Pydantic data schemas for request/response validation.

### 👤 Action Items for You:
- None required yet! Review Phase 1 and approve proceeding to Phase 2.

---

## 📌 Phase 3: Core AI & Scoring Engine (UPCOMING)
- Consolidate scoring logic into `backend/services/scoring_service.py` (0-100 normalized score).
- Send complete hardware specifications (RAM, Storage, Battery, Camera) to Gemini.
- Enforce strict JSON Schema outputs using Gemini SDK native JSON mode.

---

## 📌 Phase 4: FastAPI Backend API Server (UPCOMING)
- Create `backend/main.py` REST API server.
- Endpoints: `GET /api/v1/products/search`, `POST /api/v1/recommend`, `POST /api/v1/chat`.

---

## 📌 Phase 5: Vector DB (ChromaDB) & RAG (UPCOMING)
- Set up ChromaDB vector database for semantic search on specs & user reviews.

---

## 📌 Phase 6: Streamlit Frontend & Chatbot UI (UPCOMING)
- Connect Streamlit to FastAPI REST API.
- Add multi-turn interactive AI Chatbot tab using `st.chat_message`.

---
*Last Updated: Phase 1 Complete*
