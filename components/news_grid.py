"""
This module contains the grid component that displays multiple NewsCards with articles for the user to browse.
"""
import streamlit as st
from components.news_card import NewsCard

GRID_DIMENSIONS = (3,3)

def NewsGrid():
    cols = st.columns(GRID_DIMENSIONS[1], gap="medium") # Create columns

    for idx1, col in enumerate(cols):
        with col:
            for idx2, _ in enumerate(range(GRID_DIMENSIONS[0])):
                NewsCard(col, f'{idx1}{idx2}') # Row Card for each column
