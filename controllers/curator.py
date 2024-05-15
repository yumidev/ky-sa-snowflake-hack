"""
This module is in charge of narrowing down and organizing the articles to be shown to the user.
"""

import os
from dotenv import load_dotenv
import datetime
import requests
load_dotenv()

def get_articles_from_guardian():
    DOMAIN_NAME = "https://content.guardianapis.com"

    today = datetime.date.today()
    yesterday = (today - datetime.timedelta(days=1)).isoformat()
    tomorrow = (today + datetime.timedelta(days=1)).isoformat()


    filter_keys = ["section", "from-date", "to-date", "api-key"]
    filter_values = ["technology", yesterday, tomorrow, os.getenv("GUARDIAN_KEY")]
    filter_list = [f"{a}={b}" for a, b in zip(filter_keys, filter_values)]
    filters_concat = "&".join(filter_list)

    response = requests.get(f"{DOMAIN_NAME}/search?{filters_concat}")
    return response.json()


def get_scraped_articles():
    #FIXME
    pass
    # import pandas as pd
    # from bs4 import BeautifulSoup
    # from selenium import webdriver
    # from selenium.webdriver.chrome.options import Options

    # options = Options()
    # options.add_argument("--headless=new")
    # driver = webdriver.Chrome(options=options)
    # driver.get("https://sandbox.oxylabs.io/products")
    # content = driver.page_source
    # soup = BeautifulSoup(content, "html.parser")
    # pass

    # driver.get("https://www.bbc.com/innovation/artificial-intelligence")
