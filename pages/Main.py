"""
This module contains the code for the view aspects of the main page.
"""

import streamlit as st
from components.nav import Navbar
from components.news_grid import NewsGrid

from controllers.prompt_handler import get_cortex_response

def get_generated_text():
    st.session_state["gen_text"] = get_cortex_response("Hello world!")

def show_page():
    Navbar()
    
    st.title("Snowflake Hackathon")

    st.button("Get generated text", type="primary", on_click=get_generated_text)

    if "gen_text" not in st.session_state:
        st.session_state["gen_text"] = ""

    st.write(st.session_state["gen_text"])
    NewsGrid()
