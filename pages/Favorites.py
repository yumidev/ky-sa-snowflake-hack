"""
This module contains the code for the view aspects of the favorites page.
"""

import streamlit as st
from components.nav import Navbar
from controllers.prompt_handler import get_cortex_response
from controllers.db_handler import insert_data_and_create_table_if_not_exists


st.set_page_config(
    page_title="Bellman - Favorites",
    page_icon="🤖",
)

Navbar()
st.title("Favorites")

def on_click_save_data():
    # TODO: replace below data and schema
    data = [[5, 6], [7, 8]]
    schema = ["a", "b"]
    insert_data_and_create_table_if_not_exists(data, schema)

st.button("Click to use db", on_click=on_click_save_data)
