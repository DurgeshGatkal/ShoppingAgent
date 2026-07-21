import streamlit as st


def show_product_details(product):
    """
    Displays complete information
    about the selected product.
    """

    st.divider()

    st.header("📦 Product Details")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            product["image"],
            use_container_width=True
        )

    with col2:

        st.subheader(product["name"])

        st.write(f"🏪 Platform : {product['platform']}")

        st.write(f"💰 Price : ₹{product['price']:,}")

        st.write(f"⭐ Rating : {product['rating']}")

        st.write(f"📝 Reviews : {product['reviews']}")

        st.write(f"🎁 Offers : {product['offers']}")

        st.write(f"🚚 Delivery : {product['delivery']}")

    st.divider()

    st.subheader("📱 Specifications")

    specs1, specs2 = st.columns(2)

    with specs1:

        st.write(f"**Brand :** {product['brand']}")

        st.write(f"**Storage :** {product['storage']}")

        st.write(f"**RAM :** {product['ram']}")

        st.write(f"**Display :** {product['display']}")

    with specs2:

        st.write(f"**Processor :** {product['processor']}")

        st.write(f"**Battery :** {product['battery']}")

        st.write(f"**Camera :** {product['camera']}")

        st.write(f"**Color :** {product['color']}")

    st.divider()

    st.subheader("📖 Description")

    st.write(product["description"])

    st.divider()

    st.subheader("🤖 AI Recommendation")

    st.info(
        "Gemini AI recommendations will appear here in the next phase."
    )

    st.divider()

    st.link_button(
        "🛒 Buy Now",
        product["url"],
        use_container_width=True
    )
    