import streamlit as st

import bot

st.set_page_config(
    page_title="AI News",
    page_icon="🤖",
)

st.sidebar.success("Check your favorite articles.")

st.title("Snowflake Hackathon")

bot.add_ai_textbox()