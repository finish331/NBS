import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import json
# 目標URL網址
URL = "https://stats.nba.com/teams/"

class TeamPictureCrawler:
    def __init__(self, url):
        self.url_to_crawl = url
        self.links = []
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

    def parse(self):
        self.start_driver()     # 開啟 WebDriver
        self.get_page(self.url_to_crawl)
        self.get_links()
        self.close_driver()     # 關閉 WebDriver

    def get_links(self):
        res = BS(self.driver.page_source, 'lxml')
        temps = res.select('.stats-team-list__link')
        for link in temps:
            self.links.append(link.get('href'))

    def get_team(self):
        res = BS(self.driver.page_source, 'lxml')
        team = {}
        team_city = res.select('.stats-team-summary__city')[0].text
        team_name = res.select('.stats-team-summary__name')[0].text
        team["name"] = team_city + " " + team_name
        team["pic_url"] = self.driver.find_element_by_xpath("*//img[@class='team-logo away team-img']").get_attribute('src')
        self.result.append(team)

    def parse_detail(self):
        domain = "https://stats.nba.com"
        self.start_driver()
        for link in self.links:
            self.get_page(domain + link)
            self.get_team()
        self.close_driver()

def save_to_json(result):
    with open("team_pic.json", 'w') as file_object:
        json.dump(result, file_object)

if __name__ == '__main__':
    crawler = TeamPictureCrawler(URL)
    crawler.parse()
    crawler.parse_detail()
    save_to_json(crawler.result)
