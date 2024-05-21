"""
This module is expected to be called periodically to update the articles database
"""

import sys
sys.path.append(".")

from controllers.api_handler import get_rss_feed_data, rss_feeds
from controllers.article_controller import filter_articles_by_relevance, set_categories, articles_list_to_dataframe
from controllers.db_handler import insert_data_and_create_table_if_not_exists
from controllers.article_controller import get_ai_text, get_article_content, article_prompts

# 1. Read articles from news sources

def article_is_excluded(article, feed):
    ## If an article type is excluded, skip it
    exclusions = feed.get("exclusions", [])
    url_paths = article.link.split("/")

    return any(exclusion in url_paths for exclusion in exclusions)


def get_ai_texts(article):
    article_content = get_article_content(article)
    if article_content is None:
        return  {
        purpose: "" for purpose in article_prompts.keys()
    }
    
    ai_texts = {
        purpose: get_ai_text(article_content, prompt) for purpose, prompt in article_prompts.items()
    }

    return ai_texts


all_new_articles = []
for feed_key, feed_attrs in rss_feeds.items():
    selector = feed_attrs["selector"]

    articles = get_rss_feed_data(feed_key, feed_attrs["url"])
    articles = filter(lambda article: not article_is_excluded(article, feed_attrs), articles)
    all_new_articles.extend(articles)
    
filtered_articles = filter_articles_by_relevance(all_new_articles, "Artificial Intelligence")
set_categories(filtered_articles)

articles_df = articles_list_to_dataframe(filtered_articles)
insert_data_and_create_table_if_not_exists(articles_df, table="Article")