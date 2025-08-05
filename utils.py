import streamlit as st

def init_session():
    if 'cart' not in st.session_state:
        from cart import Cart
        st.session_state.cart = Cart()
