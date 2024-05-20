"""
This module contains the card component where news articles are shown and given certain formatting.
"""

import streamlit as st
from components.news_card_detail import card_detail

CARD_HEIGHT = 350

def NewsCard(column, index, article):
    headline = article.get("headline")
    thumbnail_url = article.get("thumbnail_url")
    
    detail_data = dict(headline=headline, thumbnail_url=thumbnail_url)
    
    card = column.container(height=CARD_HEIGHT, border=False) #creates a new container in the column
    card.markdown(f"![Image - {headline}]({thumbnail_url})")
    card.markdown(f"### {headline}")
    st.button(
        'Read summary',
        key=index,
        on_click=card_detail,
        kwargs=detail_data,
        help="See summary and key takeaways")
