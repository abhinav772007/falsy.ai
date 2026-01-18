import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWSAPI_API_KEY")

BASE_URL = "https://newsapi.org/v2/everything"

def fetch_news(query: str):
    params = {
        "apiKey": API_KEY,
        "q": query,
        "language": "en",
        "pageSize": 20,
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

    return data.get("articles", [])


def print_articles(articles):
    if not articles:
        print("No articles found.")
        return

    print(f"\nFound {len(articles)} articles:\n")

    for idx, article in enumerate(articles, 1):
        print(f"--- Article {idx} ---")
        print("source_id   :", article.get("source").get("id"))
        print("source_name :", article.get("source").get("name"))
        print("author      :", article.get("author"))
        print("title       :", article.get("title"))
        print("description :", article.get("description"))
        print("url         :", article.get("url"))
        print("urlToImage  :", article.get("urlToImage"))
        print("publishedAt :", article.get("publishedAt"))
        print("content     :", article.get("content"))
        print()


if __name__ == "__main__":
    articles = fetch_news("onepiece")
    print_articles(articles)
