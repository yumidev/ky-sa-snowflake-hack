"""
This module contains the card component where news articles are shown and given certain formatting.
"""

import streamlit as st
from components.news_card_detail import card_detail

CARD_HEIGHT = 400

def on_click_favorite(article_headline):
    if "favorites" not in st.session_state:
        st.session_state.favorites = [article_headline]
    else:
        if article_headline in st.session_state.favorites:
            st.session_state.favorites.remove(article_headline)
        else:
            st.session_state.favorites.append(article_headline)

def get_favorite_button_icon(article_headline):
    if "favorites" not in st.session_state:
        st.session_state.favorites = []
    if article_headline in st.session_state.favorites:
        return ":star:"
    else:
        return "☆"

def get_help_text(article_headline):
    if "favorites" not in st.session_state:
        st.session_state.favorites = []
    if article_headline in st.session_state.favorites:
        return "Remove from favorites"
    else:
        return "Add to favorites"

def preprocess_card_detail(article):
    st.session_state["messages"] = []
    card_detail(article)

def NewsCard(column, index, article):
    headline = article.get("headline")
    thumbnail_url = article.get("thumbnail_url")
    source = article.get("source_name")
    category = article.get("category")
    
    col_summary, col_favorite = st.columns([3,1])

    with col_summary:
        if st.button("View", key=index, help="See summary and key takeaways"):
            preprocess_card_detail(article)
    with col_favorite:
        help_text = get_help_text(headline)
        icon = get_favorite_button_icon(headline)
        st.button(icon, key=f'{index}-favorite', help=help_text, on_click=on_click_favorite, kwargs=dict(article_headline=headline), type="secondary")

    card = column.container(height=CARD_HEIGHT, border=False) #creates a new container in the column
    card.markdown(f"![Image - {headline}]({thumbnail_url})")
    card.markdown(f"### {headline}")
    source_and_category = f''':gray[Source: {source}]  
    :gray[#{category}]
    '''
    card.markdown(source_and_category)
