# BuySense AI — Development & Execution Guide

This document is your living tracker for the entire BuySense AI rebuild. It details all technical changes completed by the AI Assistant in each phase, along with specific **action items for you (the developer)**.

---

## 🚨 IMPORTANT SECURITY FIX (API Key & Git Push Issues)

### Why GitHub Blocked Your Push:
GitHub has automated secret scanners. A real Google Gemini API Key was accidentally pasted into `.env.example`. Since `.env.example` is tracked by Git, GitHub detected the secret key and blocked your push to protect your account.

### How We Fixed It:
1. **Cleaned `.env.example`**: Replaced the real key with the dummy placeholder `GEMINI_API_KEY=your_gemini_api_key_here`.
2. **Updated `.gitignore`**: Ensured `.env`, `*.env`, `database/*.db`, and cache folders are strictly ignored so secrets and binary database files never get pushed to GitHub.

### 👤 Action Required by You:
1. **Revoke the Leaked API Key**: Go to [Google AI Studio API Keys](https://aistudio.google.com/app/apikey), delete the key that was exposed, and click **Create API Key** to get a fresh new key.
2. **Put Key ONLY in `.env`**:
   - `.env` (Ignored by Git, stays on your computer only):
     ```env
     GEMINI_API_KEY=your_new_actual_gemini_api_key_here
     ```
   - `.env.example` (Tracked by Git for public GitHub):
     ```env
     GEMINI_API_KEY=your_gemini_api_key_here
     ```
3. **Commit & Push to GitHub**:
   Run the following commands in your terminal:
   ```bash
   git add .env.example .gitignore DEVELOPMENT_GUIDE.md backend/ database/
   git commit -m "Fix secret key leak in env.example and complete Phase 2 DB setup"
   git push origin main
   ```

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

## 📌 Phase 3: Core AI & Scoring Engine (NEXT UP ⏳)

### 🎯 Objective:
Build a unified, category-aware **Product Scoring Service** and update Gemini AI integration to pass hardware specifications and enforce strict JSON output formatting.

### 🛠️ Planned Changes:
1. Create `backend/services/scoring_service.py`: Replace legacy formulas with normalized 0–100 weighted score.
2. Create `backend/services/ai_service.py`: Pass complete hardware specs to Gemini and use native Gemini JSON mode (`response_schema`).
3. Refactor `backend/ai/recommendation_engine.py`: Use new AI service and unified scoring.

---
*Last Updated: Git Security Fix & Phase 2 Complete*
