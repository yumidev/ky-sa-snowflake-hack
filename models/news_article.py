"""
This module contains data associated with news articles. 
"""
from datetime import datetime

class NewsArticle():
    category:str = "" 

    def __init__(self, headline:str="", summary:str="", link:str="", timestamp:datetime=datetime.now(), thumbnail_url:str="", source_name:str=""):
        self.headline = headline
        self.summary = summary
        self.link = link
        self.timestamp = timestamp
        self.thumbnail_url = thumbnail_url
        self.source_name = source_name
    
    def __iter__(self):
        yield "headline", self.headline
        yield "summary", self.summary
        yield "link", self.link
        yield "timestamp", self.timestamp
        yield "thumbnail_url", self.thumbnail_url
        yield "source_name", self.source_name
        yield "category", self.category

    def get(self, attribute, fallback_value=None):
        return dict(self).get(attribute, fallback_value)
