import scrapy
from bs4 import BeautifulSoup as BS
import json
import requests

# class Test(scrapy.Spider):
#     name = 'test'
#     custom_settings = {
#         "USER_AGENT": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36"
#     }
#     start_urls=['https://stats.nba.com/players/list/?Historic=Y']
# 
#     def parse(self, response):
#         res = BS(response.body, 'lxml')
#         players = res.select('.players-list__name')
#         # print(players)
#         # for player in players:
#         #     print(player.text)
#         print(players)
res = requests.get('')
