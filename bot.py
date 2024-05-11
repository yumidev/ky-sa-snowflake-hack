import streamlit as st
from snowflake.snowpark import Session
from dotenv import load_dotenv
import os

load_dotenv()

connection_parameters = {
   "account": os.getenv("SNOWFLAKE_ACCOUNT"),
   "user": os.getenv("SNOWFLAKE_USER"),
   "password": os.getenv("SNOWFLAKE_PASS"),
   "warehouse": os.getenv("SNOWFLAKE_WH")
 }

session = Session.builder.configs(connection_parameters).create()  
chosen_model = "snowflake-arctic"

def add_ai_textbox():
  with st.container():
      st.header("Sample Arctic Interface")
      st.text("A summary will appear below the textbox once submitted.")
      text = st.text_area("Enter text",label_visibility="hidden", height=100, placeholder="Enter text here...")
      if text:
        text = text.replace("'", "\\'")
        prompt = f"Summarize this text in one or two sentences: {text}"
        cortex_prompt = f"'[INST]{prompt}[INST]'"
        cortex_response = session.sql(f"select snowflake.cortex.complete('{chosen_model}', {cortex_prompt}) as response").to_pandas().iloc[0]['RESPONSE']
        st.write(cortex_response)
