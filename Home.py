import streamlit as st

st.set_page_config(
    page_title="OCW WRAMS")

st.markdown("<h1 style='text-align: center';>O'Connell Whiskey Merchants</h1><h1>Warehouse Records & Management System</h1>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: left';>Created: August 28, 2023</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left';>Version 1.0.1</h6>", unsafe_allow_html=True)

st.markdown("""This simple web app is designed for easy updating to O'Connell Whiskey Merchants Warehouse inventory & records, specifically regarding:""")

st.markdown("""
    - Cask Inventory
    - Dry Goods / Packaged Goods Inventory
    - Product Planning / Cutting""")

st.markdown("""By using the menu to the left, you can select whether you'd like to add, update or delete a cask; add, update or delete dry goods; or plan a product and determine water amounts required for cutting""")

st. markdown("<h6>For help with the app, reach out to Tome!</h6>", unsafe_allow_html=True)


