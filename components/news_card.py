"""
This module contains the card component where news articles are shown and given certain formatting.
"""

import streamlit as st
from components.news_card_detail import card_detail

CARD_HEIGHT = 350

def preprocess_card_detail(article):
    st.session_state["messages"] = []
    card_detail(article)


def NewsCard(column, index, article):
    headline = article.get("headline")
    thumbnail_url = article.get("thumbnail_url")
    col_summary, col_favorite = st.columns([3,1])

    with col_summary:
        if st.button("View", key=index, help="See summary and key takeaways"):
            preprocess_card_detail(article)
    with col_favorite:
        st.button(':star:', key=f'{index}-favorite', help="Save in favorites")

    card = column.container(height=CARD_HEIGHT, border=False) #creates a new container in the column
    card.markdown(f"![Image - {headline}]({thumbnail_url})")
    card.markdown(f"### {headline}")