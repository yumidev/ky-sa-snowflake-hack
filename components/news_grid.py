"""
This module contains the grid component that displays multiple NewsCards with articles for the user to browse.
"""
import streamlit as st
from components.news_card import NewsCard

def NewsGrid():
    cols = st.columns(3, gap="medium") # Create 3 columns

    for col in cols:
        with col:
            for _ in range(3):
                NewsCard(col)