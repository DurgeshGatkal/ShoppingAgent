import streamlit as st


def show_product_card(product):
    """
    Displays one product card.
    """

    with st.container(border=True):

        st.image(product["image"], use_container_width=True)

        st.markdown(f"### {product['name']}")

        st.write(f"🏪 **Platform:** {product['platform']}")

        st.write(f"⭐ **Rating:** {product['rating']} ({product['reviews']} Reviews)")

        st.write(f"💰 **Price:** ₹{product['price']:,}")

        st.write(f"🚚 {product['delivery']}")

        st.write(f"🎁 {product['offers']}")

        if st.button(
            "View Details",
            key=f"details_{product['id']}"
        ):
            st.session_state.selected_product = product

            