"""
This module contains the navigation component that allows the user to hop between various parts of the page.
"""

import streamlit as st

def Navbar():
    with st.sidebar:
        st.page_link("app.py", label="Main Page")
        st.page_link("pages/Favorites.py", label="Favorites")
