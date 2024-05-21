"""
This module contains the card component where news articles are shown and given certain formatting.
"""

import streamlit as st
from components.news_card_detail import card_detail

CARD_HEIGHT = 350

def preprocess_card_detail(article, index):
    st.session_state["messages"] = []
    card_detail(article, index)


def NewsCard(column, index, article):
    headline = article.get("headline")
    thumbnail_url = article.get("thumbnail_url")
    
    card = column.container(height=CARD_HEIGHT, border=False)
    card.markdown(f"![Image - {headline}]({thumbnail_url})")
    card.markdown(f"### {headline}")
    if st.button("View", key=index, help="See summary and key takeaways"):
        preprocess_card_detail(article, index)