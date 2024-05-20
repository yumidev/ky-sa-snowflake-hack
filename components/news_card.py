"""
This module contains the card component where news articles are shown and given certain formatting.
"""

import streamlit as st
from components.news_card_detail import card_detail

CARD_HEIGHT = 400

def NewsCard(column, index, article):
    sample_img = "statics/imgs/the-new-york-times-logo.jpg" #TODO: Remove this in final version as this is just for testing

    card = column.container(height=CARD_HEIGHT, border=False) #creates a new container in the column
    card.image(sample_img)

    headline = article.get("headline")
    card.markdown(f"### {headline}")
    st.button('Read summary', key=index, on_click=card_detail, kwargs=dict(idx=f'{index}'), help="See summary and key takeaways")
