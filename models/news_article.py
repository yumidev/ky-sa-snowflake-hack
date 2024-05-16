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

