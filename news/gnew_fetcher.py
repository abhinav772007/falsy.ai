import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("gnew_api")
BASE_URL = "https://gnews.io/api/v4/search"
def fetch_news(query, max_results=10):
    params = {
        "q": query,
        "lang": "en",
        "country":"in",
        "max": max_results,
        "apikey": API_KEY
    }
    print(f"\n Fetching news from GNews for query → {query}")
    
    full_url = requests.Request('GET', BASE_URL, params=params).prepare().url
    print(f"API Request URL: {full_url}")
    
    response = requests.get(BASE_URL, params=params, timeout=20)


    data = response.json()
    return data.get("articles", [])
def print_articles(articles):
    if not articles:
        print(" No articles found.")
        return

    print(f"\n Found {len(articles)} articles:\n")

    for idx, article in enumerate(articles, 1):
        print(f"--- Article {idx} ---")
        print("Title       :", article.get("title"))
        print("Source      :", article.get("source", {}).get("name"))
        print("Published   :", article.get("publishedAt"))
        print("Description :", article.get("description"))
        print("URL          :", article.get("url"))
        print()
if __name__ == "__main__":
    query = "telangana temperature"
    articles = fetch_news(query)
    print_articles(articles)
