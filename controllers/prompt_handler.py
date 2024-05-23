"""
This module is in charge of connecting with LLMs and exposing LLM output to the rest of the app.
"""
import os
import sys

from dotenv import load_dotenv
from snowflake.snowpark import Session
import numpy as np
from numpy import ndarray
from sentence_transformers import SentenceTransformer

sys.path.append(".")
from utils.text_processing import clean_value

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
        raise ValueError("Prompt Handler did not receive a valid text.")
    
    user_input_trimmed = clean_value(user_input)
    prompt = f"{request} {user_input_trimmed}"
    cortex_prompt = f"'[INST]{prompt}[INST]'"
    cortex_response = session.sql(f"select snowflake.cortex.complete('{chosen_model}', {cortex_prompt}) as response").to_pandas().iloc[0]['RESPONSE']
    return cortex_response


def get_class_relevance_scores(sentences:list[str], eval_classes:list) -> ndarray:
    """
    Calculates cosine similarity scores between a set of strings and a set of classes for classification.

    Accepts a list of 1 element for binary classification.

    Returns a ndarray where rows correspond to each article, and columns correspond to each class.
    """

    # Load pre-trained model
    model_name = "Snowflake/snowflake-arctic-embed-m"
    model = SentenceTransformer(model_name)

    # Get the embeddings
    query_embeddings = model.encode(eval_classes, prompt_name="query")
    embeddings = model.encode(sentences)

    if len(eval_classes) == 1:
        scores = np.matmul(np.array(query_embeddings), embeddings.T)
    else:
        scores =  np.matmul(query_embeddings, embeddings.T)

    return scores
