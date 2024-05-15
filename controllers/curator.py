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
    import pandas as pd
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.firefox.service import Service as FFService
    from selenium.webdriver.common.by import By

    options = Options()
    options.add_argument("--headless")
    service = FFService(executable_path="/snap/bin/geckodriver")
    driver = webdriver.Firefox(options=options, service=service)
    driver.get('https://www.bbc.com/innovation/artificial-intelligence')
    blog_titles = driver.find_elements(By.CSS_SELECTOR, 'h2.bvDsJq')
    for title in blog_titles:
        print(title.text)
    driver.quit()  # closing the browser