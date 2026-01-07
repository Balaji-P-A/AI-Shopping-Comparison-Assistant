import streamlit as st
import json
from query_parser import parse_query
from comparator import compare_products

# Page configuration
st.set_page_config(
    page_title="AI Shopping Comparison Assistant",
    layout="centered"
)

st.title("🛍️ AI Shopping Comparison Assistant")
st.write("Compare products and understand trade-offs before buying.")

# Load product data
@st.cache_data
def load_products():
    with open("data/products.json", "r") as f:
        return json.load(f)

products = load_products()

# User input
user_query = st.text_input(
    "Enter your requirement:",
    placeholder="e.g. Bluetooth earphones under ₹1500 for online classes"
)

if st.button("Compare Products"):

    if user_query.strip() == "":
        st.warning("Please enter your requirement.")
    else:
        # Parse user query
        intent = parse_query(user_query)

        budget = intent.get("budget")
        usage = intent.get("usage")

        # Filter products by budget
        filtered_products = [
            p for p in products if p["price"] <= budget
        ]

        if not filtered_products:
            st.error("No products found within your budget.")
        else:
            # Compare products
            ranked_products = compare_products(filtered_products, usage)

            st.subheader("🔍 Comparison Results")

            for idx, (product, score, reason) in enumerate(ranked_products, start=1):
                with st.container():
                    st.markdown(f"### {idx}. {product['name']}")
                    st.write(f"💰 **Price:** ₹{product['price']}")
                    st.write(f"⭐ **Rating:** {product['rating']}")
                    st.write(f"🔋 **Battery:** {product['battery']} hrs")
                    st.write(f"🎤 **Mic Quality:** {product['mic_quality']}")

                    st.markdown("**Why this product?**")
                    st.info(reason)

                    st.divider()

            # Final recommendation
            best_product = ranked_products[0][0]
            st.success(
                f"✅ **Recommended Choice:** {best_product['name']} "
                f"because it best matches your requirement."
            )

st.markdown("---")
st.caption("🎓 College Project | AI Shopping Comparison Assistant")
