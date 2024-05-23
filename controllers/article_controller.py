import sys
from time import sleep
    
import numpy as np
import pandas as pd
from selenium.webdriver.common.by import By

sys.path.append(".")
from models.news_article import NewsArticle
from controllers.prompt_handler import get_class_relevance_scores, get_cortex_response
from controllers.api_handler import rss_feeds
from controllers.db_handler import get_one
from utils.selenium_handler import get_selenium_driver

driver = None

CATEGORIES = [
    "Business",
    "Innovation",
    "Chatbots",
    "Government Policy",
    "Security", 
    "Ethics & Society",
]

article_prompts = {
    "ai_summarize": f"""
    You are a news reading assistant.
    Provide a brief summary of the article provided in two to three sentences. 
    Make it insightful and engaging. Do NOT exceed three sentences. Do not repeat the article content, paraphrase the article content.
    """,
    "ai_explain": f"""
    You are a news reading assistant.
    Break down technical concepts or jargon in the article in list, and explain each term in a way that is brief, informative and simple to follow. 
    Finally, in a short two-sentence paragraph, explain how they all add up. Do NOT exceed three sentences.
    Do not repeat the article content, paraphrase the article content.
    Follow markdown format.
    """,
    "ai_takeaways": f"""
    You are a news reading assistant.
    Provide a list of three to five bullet points describing the most important, salient takeaways in this article. 
    Make them brief, impactful and engaging. Do not repeat the article content, paraphrase the article content.
    Follow markdown format.
    """,
    "ai_justify": f"""
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


def _get_article_content_thru_db(article):
    db_article = get_one("headline", article.get("headline"), table="article")


    if not db_article or not (set(article_prompts.keys()).issubset(set(db_article.keys()))):
        return None
    else:
        keys_to_join = article_prompts.keys()

        joined_content = " ".join([db_article.get(key, "") for key in keys_to_join])
    
    return joined_content
    

def _get_article_content_thru_selenium(article):
    # Get article content
    driver.get(article.get("link"))
    
    selector = rss_feeds.get(article.get("source_name"), {}).get("selector")

    article_content = None
    try:
        article_content = driver.find_elements(By.CSS_SELECTOR, selector)
    except Exception as e:
        print("An error occcured: ", e)
    finally:
        if not article_content:
            try:
                # If content list is empty, have the driver try a few times
                    RETRIES = 2
                    counter = 0
                    while counter < RETRIES and len(article_content) == 0:
                        sleep(5)
                        article_content = driver.find_elements(By.CSS_SELECTOR, selector)
            except Exception as e:
                print("Failed to initialize content upon retry. Error:", e)
            

    # Combine all the article content
    article_content_str = article_content[0].text

    return article_content_str


#TODO: implement this function
def _get_article_content_thru_beatifulsoup(article):
    from bs4 import BeautifulSoup
    import requests

    url = article.get("link")
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    try:
        articles = soup.find_all("article").children

        article_content_str = ""
        for element in articles:
            article_content_str = article_content_str + element.text
    except Exception as e:
        return None
    
    return ValueError

def get_article_content(article):
    global driver
    article_content = None

    methods = [
        _get_article_content_thru_db,
        _get_article_content_thru_beatifulsoup,
        _get_article_content_thru_selenium
    ]

    method_names = [
        "db",
        "beautifulsoup",
        "selenium"
    ]

    method_name = None
    for i, method in enumerate(methods):
        if article_content is None:
            if method_names[i] == "selenium":
                driver = get_selenium_driver()
        
                if driver is None:
                    return None
    
            article_content = method(article)
            method_name = method_names[i]

    return (article_content, method_name)

def get_ai_text(article_content, chosen_prompt=article_prompts["ai_summarize"]):
    return get_cortex_response(article_content, chosen_prompt)
