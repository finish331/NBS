import time
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import json
import os
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
# 目標URL網址
URL = "https://stats.nba.com/players/list/?Historic=Y"

class PlayerPictureCrawler:
    def __init__(self, url, index):
        self.url_to_crawl = url
        self.result = []
        self.links = []
        self.index = index

    def start_driver(self):
        print("啟動 WebDriver...")
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.implicitly_wait(10)

    def close_driver(self):
        self.driver.quit()
        print("關閉 WebDriver...")

    def get_page(self, url):
        # print("取得網頁...")
        self.driver.get(url)
        time.sleep(2)

    # 最後寫入檔案
    def save_to_json(self):
        file_name = "./JSON/player_pic" + self.index + ".json"
        with open(file_name, 'w') as file_object:
            json.dump(self.result, file_object)
            print(file_name + "完成！！！")

    def parse_link(self, index):
        print("取得球員列表...")
        domain = "https://stats.nba.com"
        res = BS(self.driver.page_source, 'lxml')
        temp_index = ord(index) - 65    #算這個字母開頭的球員是在section的第幾個
        section = res.select('.players-list__section')[temp_index]
        list = section.select('.players-list__name')
        # 加入所有這個字母開頭的球員
        for player in list:
            link = player.select('a')[0]
            self.links.append(domain + link.get('href'))

    def parse_player(self):
        player = {}
        res = BS(self.driver.page_source, 'lxml')
        first_name = res.select('.player-summary__first-name')[0].text
        last_name = res.select('.player-summary__last-name')[0].text
        attempts = 0
        while(attempts < 2):    #避免 StaleElementReferenceException
            try:
                player_pic_url = self.driver.find_element_by_xpath("//img[@class='player-img']").get_attribute('src')
                break
            except NoSuchElementException:  #沒有球員本身照片，NBA logo代替
                while(True):
                    try:
                        player_pic_url = self.driver.find_element_by_xpath("//img[@class='ng-isolate-scope player-img not-found']").get_attribute('src')
                        break
                    except NoSuchElementException:
                        try:
                            player_pic_url = self.driver.find_element_by_xpath("//img[@class='ng-isolate-scope player-img']").get_attribute('src')
                            break
                        except:
                            time.sleep(2)
                            pass
                break
            except StaleElementReferenceException:
                time.sleep(2)
                pass
            attempts += 1
        player["name"] = first_name + " " + last_name   # 球員名字
        player["pic_url"] = player_pic_url  # 球員圖片url
        self.result.append(player)  #將球員加入list
        print(player["name"] + " 爬取成功！")

    # 進入各個球員頁面
    def go_each_player(self):
        for link in self.links:
            self.get_page(link)
            self.parse_player()

    def parse(self):
        self.start_driver()     # 開啟 WebDriver
        self.get_page(self.url_to_crawl)    # 進入球員index
        self.parse_link(self.index)   # 取得所有球員url
        self.go_each_player()
        self.save_to_json()
        self.close_driver()     # 關閉 WebDriver

if __name__ == '__main__':
    index = input("請輸入爬蟲球員字母開頭(A~Z)，注意要大寫：")
    crawler = PlayerPictureCrawler(URL, index)
    crawler.parse()
    # endTime = time.clock()
    # time = endTime - startTime
    # print("完成耗時： ")
    # print(time)