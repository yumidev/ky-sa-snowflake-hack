"""
This module contains the card component where news articles are shown and given certain formatting.
"""

import streamlit as st
from components.news_card_detail import card_detail

CARD_HEIGHT = 350

def on_click_favorite(article_headline):
    if "favorites" not in st.session_state:
        st.session_state.favorites = [article_headline]
    else:
        if article_headline in st.session_state.favorites:
            st.session_state.favorites.remove(article_headline)
        else:
            st.session_state.favorites.append(article_headline)
    
# def get_button_type(article_headline):
#     if "favorites" not in st.session_state:
#         st.session_state.favorites = []
#     if article_headline in st.session_state.favorites:
#         return "primary"
#     else:
#         return "secondary"

def get_favorite_button_icon(article_headline):
    if "favorites" not in st.session_state:
        st.session_state.favorites = []
    if article_headline in st.session_state.favorites:
        return "☆"
    else:
        return ":star:"

def get_help_text(article_headline):
    if "favorites" not in st.session_state:
        st.session_state.favorites = []
    if article_headline in st.session_state.favorites:
        return "Remove from favorites"
    else:
        return "Add to favorites"

def NewsCard(column, index, article):
    headline = article.get("headline")
    thumbnail_url = article.get("thumbnail_url")
    
    detail_data = dict(headline=headline, thumbnail_url=thumbnail_url)

    col_summary, col_favorite = st.columns([3,1])
    with col_summary:
        st.button(
            'Read summary',
            key=index,
            on_click=card_detail,
            kwargs=detail_data,
            help="See summary and key takeaways")
    with col_favorite:
        # button_type = get_button_type(headline)
        help_text = get_help_text(headline)
        icon = get_favorite_button_icon(headline)
        st.button(icon, key=f'{index}-favorite', help=help_text, on_click=on_click_favorite, kwargs=dict(article_headline=headline), type="secondary")

    card = column.container(height=CARD_HEIGHT, border=False) #creates a new container in the column
    card.markdown(f"![Image - {headline}]({thumbnail_url})")
    card.markdown(f"### {headline}")
