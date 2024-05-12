"""
This module contains the code for the view aspects of the favorites page.
"""

import streamlit as st
from components.nav import Navbar
from controllers.prompt_handler import get_cortex_response


st.set_page_config(
    page_title="Bellman - Favorites",
    page_icon="🤖",
)

Navbar()
st.title("Favorites")
