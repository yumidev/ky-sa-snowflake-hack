"""
This module contains the news card detail component where summary and key takeaways of news article is shown.
"""

import streamlit as st
import streamlit.components.v1 as components

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in est rutrum, imperdiet ex et, lacinia mauris. Phasellus porttitor tristique nisi non tempor. Duis lacinia porta enim non consequat. In tellus nulla, rhoncus vitae mattis non, interdum in dolor. Suspendisse potenti. Etiam id arcu posuere, pellentesque justo ut, euismod orci. Curabitur nec odio et nunc interdum aliquet nec eu magna. Integer eget risus sed leo vestibulum viverra. Cras vel sapien mi. Vestibulum pretium lacinia cursus. Fusce ullamcorper interdum elit quis fringilla.'

@st.experimental_dialog("Summary", width="large")
def card_detail(headline, thumbnail_url):
    # TODO: Check if summary and key takeaways of this article exists in session state.
  
    st.header(headline)
    
    components.html(
        f"""
        <div style="display: flex; justify-content: center;">
          <img src="{thumbnail_url}" height="270">
        </div>
        """,
        width=720,
        height=270
    )
    
    tab_summary, tab_takeaways, tab_justify = st.tabs(["Summary", "Takeaways", "Justify"])

    with tab_summary:
        st.markdown(text)

    with tab_takeaways:
        st.markdown(text)

    with tab_justify:
        st.markdown(text)
