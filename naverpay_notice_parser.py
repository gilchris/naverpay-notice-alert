from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def get_notice_list():
    options = webdriver.FirefoxOptions()
    options.headless = True
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://admin.pay.naver.com/notice")

    articles = driver.find_elements(by=By.CSS_SELECTOR, value="td.tl > a")
    out = []
    for article in articles:
        out.append({
            "url": article.get_attribute("href"),
            "title": article.text
        })
    return out
