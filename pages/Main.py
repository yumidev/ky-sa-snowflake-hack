"""
This module contains the code for the view aspects of the main page.
"""

import streamlit as st
from components.nav import Navbar
from components.news_grid import NewsGrid
from components.filter import CategoryFilter

from controllers.prompt_handler import get_cortex_response
from controllers.db_handler import get_most_recent

def show_page():
    Navbar()
    
    st.title("Bellman AI")

    if "gen_text" not in st.session_state:
        st.session_state["gen_text"] = ""

    st.write(st.session_state["gen_text"])

    curated_articles = get_most_recent(9, table="article")
    # print(f'curated_articles: {curated_articles}')

    CategoryFilter()

    NewsGrid(curated_articles)