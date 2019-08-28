import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from NBS.items import NbsItem
from bs4 import BeautifulSoup as BS
import re
import pandas


class PlayerCrawler(CrawlSpider):
    name = 'playerCrawler'
    url = 'https://www.basketball-reference.com/players/'
    start_urls = []
    rules = [
        Rule(LinkExtractor(allow=('/players/a/')),
             callback='parse', follow=True)
    ]
    for alphabet in range(97, 123):
        start_urls.append(url + chr(alphabet) + '/')

    def parse(self, response):
        domain = 'https://www.basketball-reference.com'
        res = BS(response.body, 'lxml')
        table = res.select('table')[0].select('tbody')[0]   #取得球員列表
        for index in table.select('tr'):
            index = index.select('th')[0]
            url = index.select('a')[0].get('href')
            yield scrapy.Request(domain + url, self.parse_detail)   #進入各球員頁面

    def parse_detail(self, response):
        res = BS(response.body, 'lxml')
        team = None
        name = res.select('h1')[0].text  # 球員名字
        number = res.select('text')  # 球員最後一個背號
        temp = res.select('#necro-birth')[0]
        birth_year = temp.select('a')[1].text  # 球員出生年
        table = pandas.read_html(response.url)[0]  # 球員歷年數據表格
        meta = res.select('#meta')[0]  # 球員基本資料區
        meta = meta.select('p')  # 球員基本資料

        for strongStr in meta:
            if len(strongStr.select('strong')) != 0:
                if re.findall("Position", strongStr.select('strong')[0].text):
                    position = strongStr.text   #抓球員位置
                if re.findall("Team", strongStr.select('strong')[0].text):
                    team = strongStr.select('a')[0].text    #抓球員所屬球隊

        #取得球員位置
        str = re.split('\n', position)
        for i in range(len(str)):
            if str[i] == '  Position:':
                break
        position = str[i+2][2:]

        #設定ID
        id = name.replace(' ', '') + birth_year #ID為名字+出生年份

        nbsItems = NbsItem()
        nbsItems['name'] = name
        nbsItems['id'] = id
        nbsItems['number'] = number[len(number)-1].text
        nbsItems['team'] = team
        nbsItems['position'] = position
        nbsItems['data'] = table.to_dict()
        return nbsItems
