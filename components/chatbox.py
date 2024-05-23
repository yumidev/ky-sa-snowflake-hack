import sys
import streamlit as st

sys.path.append(".")
from controllers.prompt_handler import get_cortex_response
from utils.text_processing import clean_value

@st.experimental_fragment
def chatbox(article_content):
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    chat_slot = st.empty()
    
    chat_container = chat_slot.container()

    for message in st.session_state["messages"]:
        with chat_container.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask your follow-up questions."):
        chat_container.chat_message("user").markdown(prompt)

        st.session_state["messages"].append({"role": "user", "content": prompt})

        article_content_cleaned = clean_value(article_content)

        response = get_cortex_response(prompt, f"{article_content_cleaned}\n\nUse the context above to answer the user\\'s question below to the best of your ability. Answer briefly and precisely.")
        with chat_container.chat_message("Bellman"):
            st.markdown(response)

        st.session_state["messages"].append({"role": "assistant", "content": response})
