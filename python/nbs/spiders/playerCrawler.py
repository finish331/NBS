#使用Anaconda Prompt開啟檔案
#輸入scrapy startproject 'projectName' 創建專案
#輸入scrapy crawl 'fileName'執行
#輸入scrapy crawl 'fileName' -o fileName.檔案類別 -t 檔案類別 ; -o代表等一下要輸出的檔案 -t是要用的格式

import scrapy
from bs4 import BeautifulSoup as BS
from nbs.items import NbsItem
import re

class PlayerCrawler(scrapy.Spider):
    name = 'player'
    start_urls = ['https://www.basketball-reference.com/players/a/anthoca01.html']
    # start_urls = ['https://www.basketball-reference.com/players/a/arizatr01.html']
    # start_urls = ['https://www.basketball-reference.com/players/a/arlaujo01.html']

    def parse(self, response):
        team = None
        res = BS(response.body, 'lxml')

        basicData = res.select('.stats_pullout')[0]
        basicData = basicData.select('p')
        name = res.select('h1')
        number = res.select('text')
        meta = res.select('#meta')[0]
        meta = meta.select('p')

        for strongStr in meta:
            if len(strongStr.select('strong')) != 0:
                if re.findall("Position", strongStr.select('strong')[0].text):
                    position = strongStr.text
                if re.findall("Team", strongStr.select('strong')[0].text):
                    team = strongStr.select('a')[0].text

        str = re.split("\n", position)
        for i in range(len(str)):
            if str[i] == '  Position:':
                break
        position = str[i+2][2:]

        nbsItems = NbsItem()
        nbsItems['name'] = name[0].text
        nbsItems['number'] = number[len(number)-1].text
        if team == None:
            nbsItems['team'] = None
        else :
            nbsItems['team'] = team
        nbsItems['position'] = position
        nbsItems['game'] = basicData[2].text
        nbsItems['points'] = basicData[4].text
        nbsItems['rebounds'] = basicData[6].text
        nbsItems['assists'] = basicData[8].text
        nbsItems['FG'] = basicData[10].text
        nbsItems['FG3'] = basicData[12].text
        nbsItems['FT'] = basicData[14].text
        nbsItems['eFG'] = basicData[16].text
        nbsItems['PER'] = basicData[18].text
        nbsItems['WS'] = basicData[20].text
        return nbsItems

        # def exportJsom(self, response):
