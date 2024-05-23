import sys
import os
from dotenv import load_dotenv
from datetime import datetime
import requests
import feedparser

sys.path.append(".")
from models.news_article import NewsArticle

load_dotenv()

rss_feeds = {
    "BBC":{
        "url": "https://feeds.bbci.co.uk/news/technology/rss.xml",
        "selector": "article",
        "exclusions": ["sounds"]
    },
    "Wall Street Journal":{
        "url": "https://feeds.a.dj.com/rss/RSSWSJD.xml"
    },
    "Bloomberg": {
        "name": "Bloomberg",
        "url": "https://feeds.bloomberg.com/technology/news.rss"
    },
    "Forbes": {
        "url": "https://www.forbes.com/innovation/feed"
    },
    "MIT Technology Review": {},
    "IEEE Spectrum": {
        "url": "https://ieeetv.ieee.org/channel_rss/channel_7/rss"
    },
    "CNET": {
        "url": "https://www.cnet.com/rss/news/"
    },
    "The Verge": {
        "url": "https://www.theverge.com/rss/index.xml"
    }  
}

def get_articles_from_guardian():
    DOMAIN_NAME = "https://content.guardianapis.com"

    today = datetime.date.today()
    yesterday = (today - datetime.timedelta(days=1)).isoformat()
    one_week_ago = (today - datetime.timedelta(days=7)).isoformat()
    tomorrow = (today + datetime.timedelta(days=1)).isoformat()


    filter_keys = ["section", "from-date", "to-date", "api-key"]
    filter_values = ["technology", yesterday, tomorrow, os.getenv("GUARDIAN_KEY")]
    filter_list = [f"{a}={b}" for a, b in zip(filter_keys, filter_values)]
    filters_concat = "&".join(filter_list)

    response = requests.get(f"{DOMAIN_NAME}/search?{filters_concat}")
    response_json = response.json()

    articles = []

    for result in response_json.get("response").get("results"):
        article = NewsArticle(
            headline=result.get("webTitle"),
            link=result.get("webUrl"),
            timestamp=result.get("webPublicationDate"),
        )
        articles.append(article)

    return articles

def get_articles_from_nyt():
    DOMAIN_NAME = "https://api.nytimes.com"

    api_key = os.getenv("NYT_KEY")
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    
    response = requests.get(f"{DOMAIN_NAME}/svc/archive/v1/{year}/{month}.json?api-key={api_key}")
    response_json = response.json()

    articles = []

    for doc in response_json.get("response").get("docs"):
        multimedia = doc.get("multimedia", [{}])
        if multimedia and len(multimedia) > 0:
            img_url = multimedia[0].get("url")
        else:
            img_url = ""

        article = NewsArticle(
            headline=doc.get("headline").get("main"),
            summary=doc.get("abstract"),
            link=doc.get("web_url"),
            timestamp=doc.get("pub_date"),
            thumbnail_url=img_url
        )
        articles.append(article)
    
    return articles

def get_rss_feed_data(source_name, url):
    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries:
        timestamp = datetime.strptime(entry.get("published"), "%a, %d %b %Y %H:%M:%S %Z")
        
        article = NewsArticle(
            headline=entry.get("title"),
            summary=entry.get("summary"),
            link=entry.get("link"),
            timestamp=timestamp,
            thumbnail_url=entry.get("media_thumbnail", [{}])[0].get("url"),
            source_name=source_name
        )
        articles.append(article)
    
    return articles
