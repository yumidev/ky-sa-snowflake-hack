import streamlit as st
import streamlit.components.v1 as components

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in est rutrum, imperdiet ex et, lacinia mauris. Phasellus porttitor tristique nisi non tempor. Duis lacinia porta enim non consequat. In tellus nulla, rhoncus vitae mattis non, interdum in dolor. Suspendisse potenti. Etiam id arcu posuere, pellentesque justo ut, euismod orci. Curabitur nec odio et nunc interdum aliquet nec eu magna. Integer eget risus sed leo vestibulum viverra. Cras vel sapien mi. Vestibulum pretium lacinia cursus. Fusce ullamcorper interdum elit quis fringilla.'

@st.experimental_dialog("Lorem Ipsum")
def card_detail(idx):
    # TODO: Check if summary and key takeaways of this article exists in session state.
    # If it exists, render it instead of calling snowflake arctic api
  
    st.write(f"Read article {idx}")
    sample_img = "statics/imgs/the-new-york-times-logo.jpg" #TODO: Remove this in final version as this is just for testing
    st.image(sample_img)    
    
    # TODO: Adjust the width of dialog
    # TODO: Add line breaks to text
    # TODO: Replace the text with result from arctic
    st.header('Summary')
    st.text(text)
    st.header('Key Takeaways')
    st.text(text)
