"""
This module serves as an entry point for the app.

Run with: 
streamlit run app.py
"""

import sys
import streamlit as st

sys.path.insert(1, "./pages/")
sys.path.insert(1, "./components/")
from pages import Main

st.set_page_config(
    page_title="Bellman - Your One-Stop Source for AI News",
    page_icon="🤖",
)

if __name__ == "__main__":
    Main.show_page()