"""
This module contains the grid component that displays multiple NewsCards with articles for the user to browse.
"""
import streamlit as st
from components.news_card import NewsCard

GRID_DIMENSIONS = (3,3)

def cell_to_ordinal(row, col, num_columns):
    return (col * num_columns) + row

def NewsGrid(articles):
    cols = st.columns(GRID_DIMENSIONS[1], gap="medium") # Create columns

    for col_idx, col in enumerate(cols):
        with col:
            for row_idx, _ in enumerate(range(GRID_DIMENSIONS[0])):
                target_article = articles[cell_to_ordinal(row_idx, col_idx, GRID_DIMENSIONS[0])]
                NewsCard(col, f'{row_idx}{col_idx}', target_article) # Row Card for each column
