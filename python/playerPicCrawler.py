import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import json
import os
from selenium.common.exceptions import NoSuchElementException
# 目標URL網址
URL = "https://stats.nba.com/players/list/?Historic=Y"

class PlayerPictureCrawler:
    def __init__(self, url):
        self.url_to_crawl = url
        self.result = []
        self.links = []

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

    def parse_link(self):
        domain = "https://stats.nba.com"
        res = BS(self.driver.page_source, 'lxml')
        list = res.select('.players-list__name')
        for player in list:
            link = player.select('a')[0]
            self.links.append(domain + link.get('href'))

    def parse_player(self):
        player = {}
        res = BS(self.driver.page_source, 'lxml')
        first_name = res.select('.player-summary__first-name')[0].text
        last_name = res.select('.player-summary__last-name')[0].text
        try:
            player_pic_url = self.driver.find_element_by_xpath("//img[@class='player-img']").get_attribute('src')
        except NoSuchElementException:
            player_pic_url = self.driver.find_element_by_xpath("//img[@class='player-img not-found']").get_attribute('src')
        player["name"] = first_name + " " + last_name
        player["pic_url"] = player_pic_url
        self.result.append(player)
        print(player["name"] + " 爬取成功！")

    def go_each_player(self):
        for link in self.links:
            self.get_page(link)
            self.parse_player()

    def parse(self):
        self.start_driver()     # 開啟 WebDriver
        self.get_page(self.url_to_crawl)
        self.parse_link()
        self.go_each_player()
        self.close_driver()     # 關閉 WebDriver


def save_to_json(result):
    with open("./JSON/player_pic.json", 'w') as file_object:
        json.dump(result, file_object)

if __name__ == '__main__':
    crawler = PlayerPictureCrawler(URL)
    crawler.parse()
    save_to_json(crawler.result)
