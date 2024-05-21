"""
This module contains the code for the view aspects of the main page.
"""

import streamlit as st
from components.nav import Navbar
from components.news_grid import NewsGrid
from controllers.db_handler import get_most_recent

@st.cache_data(show_spinner=False)
def load_most_recent_articles():
    return get_most_recent(9, table="article")

def show_page():
    Navbar()
    
    st.title("Bellman AI")
    
    with st.spinner("Loading your AI news..."):
        curated_articles = load_most_recent_articles()

    NewsGrid(curated_articles)