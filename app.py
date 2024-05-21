"""
This module serves as an entry point for the app.

Run with: 
streamlit run app.py
"""

import sys
import streamlit as st

sys.path.append(".")
from pages.Main import show_page

st.set_page_config(
    page_title="Bellman - Your One-Stop Source for AI News",
    page_icon="🤖",
)

if __name__ == "__main__":
    show_page()