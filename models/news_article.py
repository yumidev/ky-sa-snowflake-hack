"""
This module contains data associated with news articles. 
"""

class NewsArticle():
    def __init__(self, headline, summary="", link="", timestamp="", thumbnail_url=""):
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