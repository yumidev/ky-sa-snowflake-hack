"""
This module contains the grid component that displays multiple NewsCards with articles for the user to browse.
"""
import streamlit as st
from components.news_card import NewsCard



def cell_to_ordinal(row, col, num_columns):
    return (row * num_columns) + col

# TODO: fix grid to handle any number of articles
def NewsGrid():
    if "articles" not in st.session_state:
        st.session_state["articles"] = []
    articles = st.session_state["articles"]
    num_of_articles = len(articles)
    divided = divmod(num_of_articles, 3)
    num_of_rows = divided[0] 
    remainder = divided[1]
    if remainder > 0:
        num_of_rows += num_of_rows

    GRID_DIMENSIONS = (num_of_rows, 3)
    
    cols = st.columns(GRID_DIMENSIONS[1], gap="medium") # Create columns

    for col_idx, col in enumerate(cols):
        with col:
            for row_idx, _ in enumerate(range(GRID_DIMENSIONS[0])):
                article_index = cell_to_ordinal(row_idx, col_idx, GRID_DIMENSIONS[1])
                if article_index < num_of_articles:
                    target_article = articles[article_index]
                    NewsCard(col, f'{row_idx}{col_idx}', target_article) # Row Card for each column
