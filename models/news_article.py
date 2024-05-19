"""
This module contains data associated with news articles. 
"""

class NewsArticle():
    category:str = "" 

    def __init__(self, headline:str, summary:str="", link:str="", timestamp:str="", thumbnail_url:str=""):
        self.headline = headline
        self.summary = summary
        self.link = link
        self.timestamp = timestamp
        self.thumbnail_url = thumbnail_url
    
    def __iter__(self):
        yield "headline", self.headline
        yield "summary", self.summary
        yield "link", self.link
        yield "timestamp", self.timestamp
        yield "thumbnail_url", self.thumbnail_url