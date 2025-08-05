import streamlit as st
from products import get_products
from utils import init_session

init_session()

st.set_page_config(page_title="Coffee Shop", layout="wide")
st.title("☕ E-Commerce Coffee Shop")

menu = ["Home", "Cart", "Checkout"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("🛒 Available Products")
    products = get_products()
    for p in products:
        with st.container():
            st.image(p.image_url, width=150)
            st.write(f"### {p.name} - ₹{p.price}")
            st.write(p.description)
            if st.button(f"Add to Cart {p.id}"):
                st.session_state.cart.add_item(p)
                st.success(f"{p.name} added to cart!")

elif choice == "Cart":
    st.subheader("🛒 Your Cart")
    cart_items = st.session_state.cart.get_items()
    if cart_items:
        for item in cart_items:
            st.write(f"- {item.name} - ₹{item.price}")
        st.write(f"### Total: ₹{st.session_state.cart.get_total()}")
    else:
        st.info("Your cart is empty.")

elif choice == "Checkout":
    st.subheader("✅ Checkout")
    if st.button("Place Order"):
        st.session_state.cart.clear()
        st.success("Thank you! Your order has been placed.")
