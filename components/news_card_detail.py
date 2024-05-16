import streamlit as st

@st.experimental_dialog("Lorem Ipsum")
def card_detail(idx):
    # TODO: Check if summary and key takeaways of this article exists in session state.
    # If it exists, render it instead of summarize and key takeaways buttons
  
    st.write(f"Read article {idx}")
    sample_img = "statics/imgs/the-new-york-times-logo.jpg" #TODO: Remove this in final version as this is just for testing
    st.image(sample_img)
    
    col1, col2 = st.columns([1,1])
    with col1:
        # button - summary button    
        if st.button("Summarize"):
            # TODO: Add the summary to session, so that it won't run summarize again
            # st.session_state.card_detail = {"item": idx, "summary": "summary"}
            # st.rerun()
            st.write('Summarize clicked')
    
    with col2:
        # button - key takeaways
        if st.button("Key Takeaways"):
            # TODO: Add the summary to session, so that it won't run summarize again
            # TODO: Get from session_state
            # st.session_state.card_detail = {"item": idx, "takeaways": "takeaways"}
            st.write('Key Takeaways clicked')
            
        # reason = st.text_input("Because...")
        # if st.button("Submit"):
        #     st.session_state.vote = {"item": idx, "reason": reason}
        #     st.rerun()
