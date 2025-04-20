from bs4 import BeautifulSoup
import requests
import random


def good_news_scrape():
    url = "https://www.goodnewsnetwork.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = articles = soup.find_all("h3", class_="entry-title td-module-title")
    news_list = []
    for article in articles:
        link = article.find("a")
        if link:
            href = link.get("href")
            title = link.get("title")
            news_list.append({"title": title, "link": href})

    return random.sample(news_list, min(len(news_list), 3))
