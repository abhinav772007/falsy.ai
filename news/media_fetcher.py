import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("MEDIASTACK_API_KEY")

BASE_URL = "http://api.mediastack.com/v1/news"

def fetch_news(query, limit=10):
    params = {
        "access_key": API_KEY,
        "keywords": query,
        "languages": "en",
        "country": "in",
        "limit": limit,
        "sort": "published_desc"
    }

    print(f"\nFetching news from Mediastack for query → {query}")
    

    full_url = requests.Request('GET', BASE_URL, params=params).prepare().url
    print(f" API Request URL: {full_url}")
    
    response = requests.get(BASE_URL, params=params, timeout=20)

    

    data = response.json()
    return data.get("data", [])


def print_articles(articles):
    if not articles:
        print("No articles found.")
        return

    print(f"\nFound {len(articles)} articles:\n")

    for idx, article in enumerate(articles, 1):
        print(f"--- Article {idx} ---")
        print("Title       :", article.get("title"))
        print("Source      :", article.get("source"))
        print("Published   :", article.get("published_at"))
        print("Description :", article.get("description"))
        print("URL          :", article.get("url"))
        print()

if __name__ == "__main__":
    query = "delhi"
    articles = fetch_news(query)
    print_articles(articles)
