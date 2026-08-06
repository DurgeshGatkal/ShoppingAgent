import sys
import requests
from pathlib import Path
import streamlit as st

# Load custom CSS
css_path = Path(__file__).parent / "styles.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Add project root to sys.path for backend imports
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Component and backend imports
from components.product_card import show_product_card
from backend.services.search import search_products
from components.product_details import show_product_details
from backend.ai.recommendation_engine import generate_recommendation

# Page configuration
st.set_page_config(
    page_title="BuySense AI",
    page_icon="🛍️",
    layout="wide"
)

# Session state
if "products" not in st.session_state:
    st.session_state.products = []
if "selected_product" not in st.session_state:
    st.session_state.selected_product = None
if "ai_recommendation" not in st.session_state:
    st.session_state.ai_recommendation = ""

# Custom CSS for styling (keep existing style block)
st.markdown("""<style>
.main { background-color: #F8F9FA; }
.title{ text-align:center; font-size:45px; font-weight:bold; color:#1E3A8A; }
.subtitle{ text-align:center; color:gray; font-size:20px; margin-bottom:30px; }
.search-title{ font-size:24px; font-weight:bold; }
.section-title{ font-size:26px; font-weight:bold; color:#1E3A8A; margin-top:20px; }
.footer{ text-align:center; color:gray; margin-top:50px; }
</style>""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='title'>🛍️ BuySense AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Compare Products Across Multiple Platforms with AI</p>", unsafe_allow_html=True)
st.divider()

# Hero section
left, right = st.columns([2,1])
with left:
    st.markdown("## Buy Smarter with AI")
    st.write("""Find products from multiple shopping platforms.

Compare prices.

View specifications.

Get AI recommendations.

Choose the best deal.""")
with right:
    st.image("https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600", use_container_width=True)
st.divider()

# Search section
st.markdown("<p class='section-title'>🔍 Search Products</p>", unsafe_allow_html=True)
search_query = st.text_input("", placeholder="Search for Mobiles, Laptops, Earbuds...")
search_clicked = st.button("🔍 Search", use_container_width=True)
st.divider()

# Popular searches
st.markdown("<p class='section-title'>🔥 Popular Searches</p>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.button("📱 iPhone")
with col2:
    st.button("💻 Laptop")
with col3:
    st.button("🎧 Earbuds")
with col4:
    st.button("⌚ Smartwatch")
with col5:
    st.button("📷 Camera")
st.divider()

# Search results
st.markdown("<p class='section-title'>🛒 Search Results</p>", unsafe_allow_html=True)
if search_clicked:
    products = search_products(search_query)
    result = generate_recommendation(products)
    st.session_state.products = result["ranked_products"]
    st.session_state.ai_recommendation = result["recommendation"]

if len(st.session_state.products) > 0:
    cols = st.columns(3)
    for index, product in enumerate(st.session_state.products):
        with cols[index % 3]:
            show_product_card(product)
else:
    st.info("Search for a product to begin.")
st.divider()

# Product details
if st.session_state.selected_product is not None:
    show_product_details(st.session_state.selected_product)

# AI Recommendation
if st.session_state.ai_recommendation:
    st.divider()
    st.subheader("🤖 BuySense AI Recommendation")
    rec = st.session_state.ai_recommendation
    if isinstance(rec, dict):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("🏆 Best Overall")
            st.write(rec["best_overall"]["product"])
            st.caption(rec["best_overall"]["reason"])
        with col2:
            st.info("💰 Best Budget")
            st.write(rec["best_budget"]["product"])
            st.caption(rec["best_budget"]["reason"])
        with col3:
            st.warning("⭐ Best Rated")
            st.write(rec["best_rated"]["product"])
            st.caption(rec["best_rated"]["reason"])
        st.markdown("### ✅ Final Recommendation")
        st.success(rec["final_recommendation"])
    else:
        st.error("Gemini did not return a valid recommendation.")
        st.write(rec)

# Chat UI
st.subheader("💬 Shopping Assistant")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])
user_input = st.chat_input("Ask a question about products...")
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    try:
        response = requests.post(
            "http://localhost:8000/api/v1/chat",
            json={"message": user_input, "context_products": st.session_state.products},
            timeout=30,
        )
        reply = response.json().get("reply", "Sorry, I couldn't get a response.")
    except Exception as e:
        reply = f"Error contacting chat service: {e}"
    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)

# Footer
st.markdown("""<div class='footer'>
Made with ❤️ using

Python • Streamlit • Gemini AI
</div>""", unsafe_allow_html=True)
