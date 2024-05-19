"""
This module is in charge of connecting database in snowflake.
"""

from controllers.session_handler import session

default_schema = ["headline", "summary", "link", "timestamp",  "thumnail_url", "category"]

default_table = "default_table"

# TODO: Add read data from table function

def show_table():
    session.table(default_table).show()

# insert data
def insert_data_and_create_table_if_not_exists(data, schema=default_schema, table=default_table):
    df1 = session.create_dataframe(data, schema=schema)
    df1.write.save_as_table(table, mode="append")
