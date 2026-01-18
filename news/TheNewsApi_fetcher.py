import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("THENEWSAPI_API_KEY")

BASE_URL = "https://api.thenewsapi.com/v1/news/all"

def fetch_news_all(query: str):
    params = {
        "api_token": API_KEY,
        "search": query,
        "language": "en",
        "limit": 10,
    }

    print(f"\n Fetching news for query → {query}")
    
    full_url = requests.Request('GET', BASE_URL, params=params).prepare().url
    print(f" API Request URL: {full_url}")
    
    response = requests.get(BASE_URL, params=params, timeout=20)

    if response.status_code != 200:
        return []

    data = response.json()
    if(data.get("status") == "error"):
        return []

    return data.get("data", [])


def print_articles(articles):
    if not articles:
        print("No articles found.")
        return

    print(f"\nFound {len(articles)} articles:\n")

    for idx, article in enumerate(articles, 1):
        print(f"--- Article {idx} ---")
        print("uuid        :", article.get("uuid"))
        print("title       :", article.get("title"))
        print("keywords    :", article.get("keywords"))
        print("description :", article.get("description"))
        print("url         :", article.get("url"))
        print("snippet     :", article.get("snippet"))
        print("source      :", article.get("source"))
        print() 

if __name__ == "__main__":
    articles = fetch_news_all("trump and modi")
    print_articles(articles)
