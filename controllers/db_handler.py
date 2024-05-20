"""
This module is in charge of connecting database in snowflake.
"""

import sys
sys.path.append(".")
from controllers.session_handler import session
from models.news_article import NewsArticle

# dynamically build the schema from the model keys
article = NewsArticle()
article_schema = list(dict(article).keys())

default_schema = article_schema
default_table = "default_table"

# TODO: Add read data from table function

def show_table():
    session.table(default_table).show()

# insert data
def insert_data_and_create_table_if_not_exists(data, schema=default_schema, table=default_table):
    df1 = session.create_dataframe(data, schema=schema)
    df1.write.save_as_table(table, mode="append")


def get_one(query_column, query_value, table=default_table):
    response = session.sql(f"select * from {table} where \"{query_column}\" = '{query_value}' LIMIT 1").collect()
    return response[0].as_dict()


def get_most_recent(limit_count, table=default_table):
    response = session.sql(f"select * from {table} order by \"timestamp\" desc limit {limit_count}").collect()
    recent_as_dicts = [row.as_dict() for row in response]
    return recent_as_dicts