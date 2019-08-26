# 使用Anaconda Prompt開啟檔案
# 輸入scrapy startproject 'projectName' 創建專案
# 輸入scrapy crawl 'fileName'執行
# 輸入scrapy crawl 'fileName' -o fileName.檔案類別 -t 檔案類別 ; -o代表等一下要輸出的檔案 -t是要用的格式
#scrapy crawl 'filename' --logfile='logFileName.log' 將log存入文字檔

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup as BS
from NBS.items import NbsItem
import re
import pandas


class PlayerCrawler(CrawlSpider):
    name = 'player'
    domain = 'https://www.basketball-reference.com/players/'
    start_urls = ['https://www.basketball-reference.com/players/a/']
    # for alphabet in range(97, 123):
    #     start_urls.append(domain + chr(alphabet) + '/')

    rules = [
        Rule(LinkExtractor(allow=('https://www.basketball-reference.com/players/[a-z]')), callback='parse', follow='true')
    ]

    def parse(self, response):
        domain = 'https://www.basketball-reference.com'
        res = BS(response.body, 'lxml')
        table = res.select('table')[0].select('tbody')[0]
        for index in table.select('tr'):
            index = index.select('th')[0]
            url = index.select('a')[0].get('href')
            yield scrapy.Request(domain + url, self.parse_detail)   #進入各個球員頁面

    def parse_detail(self, response):
        team = None
        res = BS(response.body, 'lxml')
        table = pandas.read_html(response.url)[0]   #球員歷年數據表格
        name = res.select('h1')     #球員名字
        number = res.select('text')     #球員最後一個背號
        birth = res.select('#necro-birth')[0]
        birth_year = birth.select('a')[1]   #球員出生年
        meta = res.select('#meta')[0]   #球員基本資料區
        meta = meta.select('p')     #球員基本資料

        for strongStr in meta:
            if len(strongStr.select('strong')) != 0:
                if re.findall("Position", strongStr.select('strong')[0].text):
                    position = strongStr.text
                if re.findall("Team", strongStr.select('strong')[0].text):
                    team = strongStr.select('a')[0].text

        #取得球員位置
        str = re.split('\n', position)
        for i in range(len(str)):
            if str[i] == '  Position:':
                break
        position = str[i+2][2:]

        #存成Json檔
        nbsItems = NbsItem()
        # nbsItems['id'] = id
        nbsItems['birth'] = birth_year.text
        nbsItems['name'] = name[0].text
        nbsItems['number'] = number[len(number)-1].text
        if team == None:
            nbsItems['team'] = None     #如果目前沒有球隊則為null
        else:
            nbsItems['team'] = team
        nbsItems['position'] = position
        nbsItems['data'] = table.to_dict()
        return nbsItems
