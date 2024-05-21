"""
This module contains a filter that modifies the list of displayed items based on various criteria.
"""

import streamlit as st
from controllers.article_controller import CATEGORIES
from controllers.db_handler import get_articles_by_categories, get_most_recent

def on_change_category_button(prev_selected_categories):
    if 'selected_categories' not in st.session_state:
        st.session_state.selected_categories = []

    if set(prev_selected_categories) != set(st.session_state.selected_categories):
        if len(st.session_state.selected_categories) != 0:

            selected_categories = st.session_state.selected_categories
            formatted_categories = map(lambda c: f"'{c}'", selected_categories)
            categories = ",".join(list(formatted_categories))

            new_articles = get_articles_by_categories(9, categories, table="article")
        
            if 'articles' not in st.session_state:
                st.session_state.articles = []
            
            st.session_state.articles = new_articles
        else:
            if 'articles' not in st.session_state:
                st.session_state.articles = []
                
            st.session_state.articles = get_most_recent(9, table="article")

def CategoryFilter():
    if 'selected_categories' not in st.session_state:
        st.session_state.selected_categories = []
  
    options = st.multiselect("Filter by category", options=CATEGORIES)
    prev_selected_categories = st.session_state["selected_categories"]
    st.session_state["selected_categories"] = options
    on_change_category_button(prev_selected_categories)
