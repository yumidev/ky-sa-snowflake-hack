"""
This module contains the code for the view aspects of the favorites page.
"""

import streamlit as st
from components.nav import Navbar
from components.news_grid import NewsGrid
from controllers.db_handler import get_articles_by_headlines


st.set_page_config(
    page_title="Bellman - Favorites",
    page_icon="🤖",
)

Navbar()
st.title("Favorites")

# move it to util
def escape_string(input_string):
    """
    Escapes special characters in a string by adding a backslash before them.
    This is useful when you need to use the string in SQL queries.

    Args:
        input_string (str): The input string to be escaped.

    Returns:
        str: The escaped string.
    """
    special_chars = ["'", '"', "\\"]

    escaped_string = ""

    for char in input_string:
        # Check if the character is a special character
        if char in special_chars:
            # If it is, add a backslash before it
            escaped_string += "\\" + char
        else:
            # If not, just add the character to the escaped string
            escaped_string += char

    return escaped_string

def show_page():
    if 'favorites' not in st.session_state:
        st.session_state.favorites = []

    favorites = st.session_state.favorites

    if len(favorites) > 0:
        formatted_favorites = map(lambda h: f"'{escape_string(h)}'", favorites)
        str_favorites = ",".join(list(formatted_favorites))
        favorite_articles = get_articles_by_headlines(9, str_favorites, table="article")

        NewsGrid(favorite_articles)
        
show_page()
