import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWSDATA_API_KEY")

BASE_URL = "https://newsdata.io/api/1/latest"

def fetch_news(query: str):
    params = {
        "apikey": API_KEY,
        "q": query,
        "language": "en"
    }

    print(f"\n Fetching news for query → {query}")
    
    # Construct and print the full URL
    full_url = requests.Request('GET', BASE_URL, params=params).prepare().url
    print(f" API Request URL: {full_url}")
    
    response = requests.get(BASE_URL, params=params, timeout=20)

    

    data = response.json()
    return data.get("results", [])


def print_articles(articles):
    if not articles:
        print(" No articles found.")
        return

    print(f"\n Found {len(articles)} articles:\n")

    for idx, article in enumerate(articles, 1):
        print(f"--- Article {idx} ---")
        print("Title       :", article.get("title"))
        print("Source      :", article.get("source_id"))
        print("Published   :", article.get("pubDate"))
        print("Description :", article.get("description"))
        print("URL          :", article.get("link"))
        print()
