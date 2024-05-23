"""
This module is in charge of creating session in snowflake.
"""

import os
from dotenv import load_dotenv
from snowflake.snowpark import Session

load_dotenv()
connection_parameters = {
   "account": os.getenv("SNOWFLAKE_ACCOUNT"),
   "user": os.getenv("SNOWFLAKE_USER"),
   "password": os.getenv("SNOWFLAKE_PASS"),
   "warehouse": os.getenv("SNOWFLAKE_WH"),
   "database": os.getenv("SNOWFLAKE_DB"),
   "schema": os.getenv("SNOWFLAKE_SCHEMA")
 }

session = Session.builder.configs(connection_parameters).create()
