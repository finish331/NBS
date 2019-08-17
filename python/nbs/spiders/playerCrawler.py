#使用Anaconda Prompt開啟檔案
#輸入scrapy startproject 'projectName' 創建專案
#輸入scrapy crawl 'fileName'執行
#輸入scrapy crawl 'fileName' -o fileName.檔案類別 -t 檔案類別 ; -o代表等一下要輸出的檔案 -t是要用的格式

import scrapy
from bs4 import BeautifulSoup as BS
from nbs.items import NbsItem

class PlayerCrawler(scrapy.Spider):
    name = 'player'
    start_urls = ['https://www.basketball-reference.com/players/a/anthoca01.html']

    def parse(self, response):
        res = BS(response.body, 'lxml').select('.stats_pullout')[0]
        res = res.select('p')
        # for item in res[0].select('p'):
        #     print(item[0].text)
        # print(res)
        nbsItems = NbsItem()
        nbsItems['game'] = res[2].text
        nbsItems['points'] = res[4].text
        nbsItems['rebounds'] = res[6].text
        nbsItems['assists'] = res[8].text
        nbsItems['FG'] = res[10].text
        nbsItems['FG3'] = res[12].text
        nbsItems['FT'] = res[14].text
        nbsItems['eFG'] = res[16].text
        nbsItems['PER'] = res[18].text
        nbsItems['WS'] = res[20].text
        return nbsItems
