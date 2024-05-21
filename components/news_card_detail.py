"""
This module contains the news card detail component where summary and key takeaways of news article is shown.
"""

import sys
import streamlit as st
import streamlit.components.v1 as components
import time


sys.path.append(".")
from controllers.article_controller import get_ai_text, get_article_content, article_prompts
from controllers.db_handler import update_row
from components.chatbox import chatbox


@st.cache_data(show_spinner=False)
def get_article_content_for_card(article):
    article_content, method = get_article_content(article)

    return article_content, method


@st.cache_data(show_spinner=False)
def get_tab_texts(article_content):
    tab_texts = {
        purpose: get_ai_text(article_content, prompt) for purpose, prompt in article_prompts.items()
    }

    return tab_texts

@st.experimental_fragment
def load_detail_data_for_card(article, slot):
    progress_text = "Loading your Bellman-generated insights..."
    my_bar = slot.progress(0, text=progress_text)
    article_content, content_method = get_article_content_for_card(article)
    my_bar.progress(50, progress_text)
    tab_texts = get_tab_texts(article_content)
    my_bar.progress(75, progress_text)
    if content_method != "db":
        update_row("headline", article.get("headline"), tab_texts, table="article")
    time.sleep(0.01)
    my_bar.empty()

    return tab_texts, article_content


@st.experimental_dialog("Article Insights", width="large")
def card_detail(article):
    headline = article.get("headline")
    thumbnail_url = article.get("thumbnail_url")

    st.header(headline)
    
    components.html(
        f"""
        <div style="display: flex; justify-content: center;">
          <img src="{thumbnail_url}" height="180">
        </div>
        """,
        width=720,
        height=200
    )

    slot_1 = st.empty()
    slot_2 = st.empty()

    if  slot_2.button("Close", key="button-close"):
        st.rerun()

    tab_texts, article_content = load_detail_data_for_card(article, slot_1)

    tab_summary, tab_breakdown, tab_takeaways, tab_justify, tab_ask = slot_1.tabs(["Summary", "Breakdown", "Takeaways", "Justify", "Ask"])

    with tab_summary:
        st.markdown(tab_texts["ai_summarize"])

    with tab_breakdown:
        st.markdown(tab_texts["ai_explain"])

    with tab_takeaways:
        st.markdown(tab_texts["ai_takeaways"])

    with tab_justify:
        st.markdown(tab_texts["ai_justify"])
    
    with tab_ask:
        chatbox(article_content)
