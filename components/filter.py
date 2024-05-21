"""
This module contains a filter that modifies the list of displayed items based on various criteria.
"""

import streamlit as st
from controllers.article_controller import CATEGORIES
from controllers.db_handler import get_articles_by_selected_categories

def on_change_category_button(prev_selected_categories):
    if 'selected_categories' not in st.session_state:
        st.session_state.selected_categories = []
    
    if set(prev_selected_categories) != set(st.session_state.selected_categories):
        new_articles = get_articles_by_selected_categories(9, st.session_state.selected_categories)
    
        if 'articles' not in st.session_state:
            st.session_state.articles = []
        
        st.session_state.articles = new_articles

def CategoryFilter():
    if 'selected_categories' not in st.session_state:
        st.session_state.selected_categories = []
  
    options = st.multiselect("Filter by category", options=CATEGORIES)
    prev_selected_categories = st.session_state["selected_categories"]
    st.session_state["selected_categories"] = options
    on_change_category_button(prev_selected_categories)
    
    # TODO: need to see updated new_articles affect the grid properly
