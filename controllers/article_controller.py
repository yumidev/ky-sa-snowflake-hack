import sys

import numpy as np

sys.path.append(".")
from models.news_article import NewsArticle
from controllers.prompt_handler import get_class_relevance_scores

def filter_articles_by_relevance(articles, topic):
    """
    Filters a list of articles based on how relevant they are to the given topic. 

    The function returns a filtered copy of the article list.
    """
    AI_RELEVANCE_THRESHOLD = 0.205

    # Concatenate headline and summary to give the model more material to calculate similarity
    headlines = [article.headline + ": " + article.summary for article in articles]
    
    # get relevance scores (range of 0 to 1) and pair the scores to each article
    relevance_scores = get_class_relevance_scores(headlines, [topic])
    score_pairs = list(zip(articles, relevance_scores[0]))
    
    # remove articles with scores below the threshold and unpair articles from scores
    # these articles are assumed to not be relevant enough to the topic
    filtered_articles_pair = filter(lambda x: x[1] > AI_RELEVANCE_THRESHOLD, score_pairs)
    filtered_articles = [pair[0] for pair in filtered_articles_pair]

    return filtered_articles


def set_categories(articles:list[NewsArticle]) -> None:
    """
    Assigns categories to articles based on instance variables such as headlines and summaries.

    The categories are set by reference.
    """

    CATEGORIES = [
        "Business",
        "Innovation",
        "Chatbots",
        "Government Policy",
        "Security", 
        "Ethics & Society",
    ]
    
    # Concatenate headline and summary to give the model more material to calculate similarity
    headlines = [article.headline + ": " + article.summary for article in articles]

    relevance_scores = get_class_relevance_scores(CATEGORIES, headlines)

    # For each headline, the category with the highest score (range from 0 to 1) is the assigned category
    for i, query_scores in enumerate(relevance_scores):
        largest_index = np.argmax(query_scores)

        articles[i].category = CATEGORIES[largest_index]

# Sample usage of functions
# from controllers.api_handler import get_rss_feed_data
# articles = get_rss_feed_data("https://feeds.a.dj.com/rss/RSSWSJD.xml")
# filtered_articles = filter_articles_by_relevance(articles, "Artificial Intelligence")
# set_categories(filtered_articles)
# for article in filtered_articles:
#     print(f"Article:{article.headline}\nCategory:{article.category}\n\n")