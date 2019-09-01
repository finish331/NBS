import scrapy
from bs4 import BeautifulSoup as BS
import json
import requests
import pandas

class Test(scrapy.Spider):
    name = 'test'
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36"
    }
    start_urls=['https://www.basketball-reference.com/teams/WAS/2019.html']
    def parse(self, response):
        res = BS(response.body, 'lxml')
        # section = res.select('#team_and_opponent')
        # tables = pandas.read_html(response.url)
        # table = pandas.read_html(str(section))[0]
        table = pandas.read_html(response.url)
        print(len(table))
