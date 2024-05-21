"""
This module contains the code for the view aspects of the main page.
"""

import streamlit as st
from components.nav import Navbar
from components.news_grid import NewsGrid
from components.filter import CategoryFilter
from controllers.db_handler import get_most_recent

def show_page():
    Navbar()
    
    st.title("Bellman AI")

    if "articles" not in st.session_state:
        curated_articles = get_most_recent(9, table="article")
        st.session_state["articles"] = curated_articles

    CategoryFilter()
    articles = st.session_state["articles"]
    NewsGrid(articles)
