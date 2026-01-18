import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("MARKETAUX_API_KEY")


BASE_URL = "https://api.marketaux.com/v1/news/all"


def fetch_news(query, limit=10):
    params = {
        "api_token": API_KEY,
        "search": query,
        "language": "en",
        "limit": limit,
        "country":"in"
    }

    print(f"\n Fetching news from MarketAux for query → {query}")
    

    full_url = requests.Request('GET', BASE_URL, params=params).prepare().url
    print(f" API Request URL: {full_url}")
    
    response = requests.get(BASE_URL, params=params, timeout=20)

    

    data = response.json()
    return data.get("data", [])

def print_articles(articles):
    if not articles:
        print(" No articles found.")
        return

    print(f"\n Found {len(articles)} articles:\n")

    for idx, article in enumerate(articles, 1):
        print(f"--- Article {idx} ---")
        print("Title       :", article.get("title"))
        print("Source      :", article.get("source"))
        print("Published   :", article.get("published_at"))
        print("Description :", article.get("description"))
        print("URL          :", article.get("url"))
        print()

if __name__ == "__main__":
    query = "gold price india"
    articles = fetch_news(query)
    print_articles(articles)
