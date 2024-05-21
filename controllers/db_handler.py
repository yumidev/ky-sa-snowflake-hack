"""
This module is in charge of connecting database in snowflake.
"""

import sys
sys.path.append(".")

import streamlit as st

from controllers.session_handler import session
from models.news_article import NewsArticle
from utils.text_processing import clean_value

# dynamically build the schema from the model keys
article = NewsArticle()
article_schema = list(dict(article).keys())

default_schema = article_schema
default_table = "default_table"

@st.cache_resource
def init_connection():
    conn = st.connection("snowflake")

    return conn
  
def show_table():
    session.table(default_table).show()

def insert_data_and_create_table_if_not_exists(data, schema=default_schema, table=default_table):
    df = session.create_dataframe(data, schema=schema)
    df.write.save_as_table(table, mode="append")


def get_one(query_column, query_value, table=default_table):

    val = clean_value(query_value)
    conn = init_connection()
    response = conn.query(f"select * from {table} where \"{query_column}\" = \'{val}\' LIMIT 1")

    if response.empty:
        return {}
    else:
        return response.to_dict(orient="records")[0]

def get_all(table=default_table):
    conn = init_connection()
    response = conn.query(f"select * from {table}")

    if response.empty:
        return {}
    else:
        return response.to_dict(orient="records")

def get_most_recent(limit_count, table=default_table):
    conn = init_connection()
    response = conn.query(f"select * from {table} order by \"timestamp\" desc limit {limit_count}", ttl=600)
    recent_as_dicts = response.to_dict(orient="records")
    return recent_as_dicts


def get_articles_by_categories(limit_count, categories, table=default_table):
    conn = init_connection()
    response = conn.query(f"select * from {table} where \"category\" in ({categories}) order by \"timestamp\" desc limit {limit_count}", ttl=600)
    response_as_dict = response.to_dict(orient="records")
    return response_as_dict
  
def get_articles_by_headlines(limit_count, headlines, table=default_table):
    conn = init_connection()
    response = conn.query(f"select * from {table} where \"headline\" in ({headlines}) order by \"timestamp\" desc limit {limit_count}", ttl=600)
    response_as_dict = response.to_dict(orient="records")
    return response_as_dict

def update_row(key_column, key_value, new_values, table=default_table):
    conn = init_connection()
    clean_key_value = clean_value(key_value)

    for col in new_values.keys():
        try:
            conn.cursor().execute(f"alter table {table} add {col} VARCHAR")
        except:
            pass

    for key, val in new_values.items():
        new_values[key] = clean_value(val)

        conn.cursor().execute_async(f"update {table} set \"{key}\" = '{new_values[key]}' where \"{key_column}\" = '{clean_key_value}'")
