"""
This module contains the card component where news articles are shown and given certain formatting.
"""

import streamlit as st

CARD_HEIGHT = 300

def NewsCard(column):
    sample_img = "statics/imgs/the-new-york-times-logo.jpg" #TODO: Remove this in final version as this is just for testing

    card = column.container(height=CARD_HEIGHT, border=False) #creates a new container in the column
    card.image(sample_img)
    card.header("Lorem Ipsum")