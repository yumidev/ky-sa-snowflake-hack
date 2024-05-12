"""
This module is in charge of connecting with LLMs and exposing LLM output to the rest of the app.
"""

import os
from dotenv import load_dotenv
from snowflake.snowpark import Session

load_dotenv()
connection_parameters = {
   "account": os.getenv("SNOWFLAKE_ACCOUNT"),
   "user": os.getenv("SNOWFLAKE_USER"),
   "password": os.getenv("SNOWFLAKE_PASS"),
   "warehouse": os.getenv("SNOWFLAKE_WH")
 }

session = Session.builder.configs(connection_parameters).create()  
chosen_model = "snowflake-arctic"

summarize_request_str = "Summarize this text in one or two sentences:"
default_request = summarize_request_str

def get_cortex_response(user_input, request = default_request):
    if not user_input or not isinstance(user_input, str):
        raise ValueError("Prompt Handler did not receive a valid text for summarization.")
    
    user_input_trimmed = user_input.replace("'", "\\'")
    prompt = f"{request} {user_input_trimmed}"
    cortex_prompt = f"'[INST]{prompt}[INST]'"
    cortex_response = session.sql(f"select snowflake.cortex.complete('{chosen_model}', {cortex_prompt}) as response").to_pandas().iloc[0]['RESPONSE']
    return cortex_response
