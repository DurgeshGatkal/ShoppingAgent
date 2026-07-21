import streamlit as st
from frontend.components.product_card import show_product_card
from backend.services.search import search_products
from frontend.components.product_details import show_product_details

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="BuySense AI",
    page_icon="🛍️",
    layout="wide"
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "products" not in st.session_state:
    st.session_state.products = []

if "selected_product" not in st.session_state:
    st.session_state.selected_product = None

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.main {
    background-color: #F8F9FA;
}

.title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#1E3A8A;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:20px;
    margin-bottom:30px;
}

.search-title{
    font-size:24px;
    font-weight:bold;
}

.section-title{
    font-size:26px;
    font-weight:bold;
    color:#1E3A8A;
    margin-top:20px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------

st.markdown(
    "<h1 class='title'>🛍️ BuySense AI</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Compare Products Across Multiple Platforms with AI</p>",
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# HERO SECTION
# -----------------------------

left, right = st.columns([2,1])

with left:

    st.markdown("## Buy Smarter with AI")

    st.write(
        """
Find products from multiple shopping platforms.

Compare prices.

View specifications.

Get AI recommendations.

Choose the best deal.
"""
    )

with right:

    st.image(
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600",
        use_container_width=True
    )

st.divider()

# -----------------------------
# SEARCH SECTION
# -----------------------------

st.markdown(
    "<p class='section-title'>🔍 Search Products</p>",
    unsafe_allow_html=True
)

search_query = st.text_input(
    "",
    placeholder="Search for Mobiles, Laptops, Earbuds..."
)

search_clicked = st.button(
    "🔍 Search",
    use_container_width=True
)

st.divider()

# -----------------------------
# POPULAR SEARCHES
# -----------------------------

st.markdown(
    "<p class='section-title'>🔥 Popular Searches</p>",
    unsafe_allow_html=True
)

col1,col2,col3,col4,col5 = st.columns(5)

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

# -----------------------------
# SEARCH RESULTS
# -----------------------------

st.markdown(
    "<p class='section-title'>🛒 Search Results</p>",
    unsafe_allow_html=True
)

# -----------------------------
# SEARCH RESULTS
# -----------------------------

if search_clicked:

    st.session_state.products = search_products(search_query)

# Display products if they exist
if len(st.session_state.products) > 0:

    cols = st.columns(3)

    for index, product in enumerate(st.session_state.products):

        with cols[index % 3]:

            show_product_card(product)

else:

    st.info("Search for a product to begin.")


st.divider()

# -----------------------------
# PRODUCT DETAILS
# -----------------------------

if st.session_state.selected_product is not None:

    show_product_details(st.session_state.selected_product)


# -----------------------------
# FOOTER
# -----------------------------

st.markdown(
"""
<div class="footer">

Made with ❤️ using

Python • Streamlit • Gemini AI

</div>
""",
unsafe_allow_html=True
)
