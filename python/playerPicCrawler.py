import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import json
# 目標URL網址
URL = "https://stats.nba.com/players/list/?Historic=Y"

class PlayerPictureCrawler:
    def __init__(self, url):
        self.url_to_crawl = url
        self.result = []

    def start_driver(self):
        print("啟動 WebDriver...")
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.implicitly_wait(10)

    def close_driver(self):
        self.driver.quit()
        print("關閉 WebDriver...")

    def get_page(self, url):
        print("取得網頁...")
        self.driver.get(url)
        time.sleep(2)

    def parse_player(self):
        res = BS(self.driver.page_source, 'lxml')
        list = res.select('.players-list__name')
        for player in list:
            print(player.get('href'))

    def parse(self):
        self.start_driver()     # 開啟 WebDriver
        self.get_page(self.url_to_crawl)
        self.parse_player()
        self.close_driver()     # 關閉 WebDriver


def save_to_json(result):
    with open("team_pic.json", 'w') as file_object:
        json.dump(result, file_object)

if __name__ == '__main__':
    crawler = PlayerPictureCrawler(URL)
    crawler.parse()
    save_to_json(crawler.result)
