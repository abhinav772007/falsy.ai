import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CURRENTNEWS_API_KEY")

BASE_URL = "https://api.currentsapi.services/v1/search"

def fetch_news(query: str):
    params = {
        "apiKey": API_KEY,
        "country": "IN",
        "keywords": query, 
        "language": "en",
        "limit": 20,
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

    return data.get("news", [])


def print_articles(articles):
    if not articles:
        print("No articles found.")
        return

    print(f"\nFound {len(articles)} articles:\n")

    for idx, article in enumerate(articles, 1):
        print(f"--- Article {idx} ---")
        print("title :", article.get("title"))
        print("image :", article.get("image"))
        print("description :", article.get("description"))
        print("category:", article.get("category"))
        print()


if __name__ == "__main__":
    articles = fetch_news("trump")
    print_articles(articles)
