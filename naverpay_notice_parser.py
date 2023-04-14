from bs4 import BeautifulSoup
import requests


def get_notice_list():
    response = requests.get("https://admin.pay.naver.com/notice")
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.css.select("td.tl > a")

    out = []
    for article in articles:
        out.append({
            "url": "https://admin.pay.naver.com" + article["href"],
            "title": article.string
        })
    return out
