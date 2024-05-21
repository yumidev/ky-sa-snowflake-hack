import sys
from time import sleep
    
import numpy as np
import pandas as pd
from selenium.webdriver.common.by import By

sys.path.append(".")
from models.news_article import NewsArticle
from controllers.prompt_handler import get_class_relevance_scores, get_cortex_response
from controllers.api_handler import rss_feeds
from utils.selenium_handler import get_selenium_driver

CATEGORIES = [
    "Business",
    "Innovation",
    "Chatbots",
    "Government Policy",
    "Security", 
    "Ethics & Society",
]

article_prompts = {
    "summarize": f"""
    You are a news reading assistant.
    Provide a brief summary of the article provided in two to three sentences. 
    Make it insightful and engaging. Do NOT exceed three sentences. Do not repeat the article content, paraphrase the article content.
    """,
    "explain": f"""
    You are a news reading assistant.
    Break down technical concepts or jargon in the article in list, and explain each term in a way that is brief, informative and simple to follow. 
    Finally, in a short two-sentence paragraph, explain how they all add up. Do NOT exceed three sentences.
    Do not repeat the article content, paraphrase the article content.
    Follow markdown format.
    """,
    "takeaways": f"""
    You are a news reading assistant.
    Provide a list of three to five bullet points describing the most important, salient takeaways in this article. 
    Make them brief, impactful and engaging. Do not repeat the article content, paraphrase the article content.
    Follow markdown format.
    """,
    "justify": f"""
    You are a news reading assistant. Your goal is to provide content that is highly related to AI.
    Briefly, justify to the user why this article should be of interest of them.
    Do not repeat the article content, paraphrase the article content.
    Make your case with confidence and charm. Do NOT exceed three sentences.
    """
}

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
    
    # Concatenate headline and summary to give the model more material to calculate similarity
    headlines = [article["headline"] + ": " + article["summary"]for article in articles]

    relevance_scores = get_class_relevance_scores(CATEGORIES, headlines)

    # For each headline, the category with the highest score (range from 0 to 1) is the assigned category
    for i, query_scores in enumerate(relevance_scores):
        largest_index = np.argmax(query_scores)

        articles[i]["category"] = CATEGORIES[largest_index]


def articles_list_to_dataframe(articles):
    articles_as_dicts = [dict(article) for article in articles]
    
    return pd.DataFrame(articles_as_dicts)


def _get_article_content_thru_selenium(article, driver):
    # Get article content
    driver.get(article.link)
    
    selector = rss_feeds.get(article.source_name, {}).get("selector")
    article_content = driver.find_elements(By.CSS_SELECTOR, selector)

    # If content list is empty, have the driver try a few times
    RETRIES = 2
    counter = 0
    while counter < RETRIES and len(article_content) == 0:
        sleep(5)
        article_content = driver.find_elements(By.CSS_SELECTOR, selector)

    # Combine all the article content
    article_content_str = ""
    for element in article_content:
        article_content_str = article_content_str + element.text

    return article_content_str


#TODO: implement this function
def _get_article_content_thru_beatifulsoup(article):
    pass


def get_article_content(article):

    driver = get_selenium_driver()
    
    if driver is not None:
        return _get_article_content_thru_selenium(article, driver)
    else:
        return _get_article_content_thru_beatifulsoup(article)


def get_ai_text(article_content, chosen_prompt=article_prompts["summarize"]):
    return get_cortex_response(article_content, chosen_prompt)
