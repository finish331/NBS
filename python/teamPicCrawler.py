import time
from selenium import webdriver
# 目標URL網址
URL = "https://stats.nba.com/teams/"
# /html/body/main/div[@class='stats-container__inner']//table[@class='category-table']/tbody/tr/td[@class='category-table__text']/a[@class='stats-team-list__link']

class TeamPictureCrawler:
    def __init__(self, url):
        self.url_to_crawl = url

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
        self.close_driver()     # 關閉 WebDriver

if __name__ == '__main__':
    crawler = TeamPictureCrawler(URL)
    crawler.parse()
