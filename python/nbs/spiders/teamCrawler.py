import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup as BS
from NBS.items import TeamItem

class TeamCrawler(CrawlSpider):
    name = 'teamCrawler'
    start_urls = ['https://www.basketball-reference.com/teams/']
    rosters = []
    stats = []

    def parse(self, response):
        url = 'https://www.basketball-reference.com'
        res = BS(response.body, 'lxml')
        table = res.select('table')[0]
        links = table.select('a')

        for link in links:
            teamItem = TeamItem()
            for year in range(2010 ,2021):
                detail = url + link.get('href') + str(year) + '.html'
                if year == 2020:
                    yield scrapy.Request(detail, self.parse_past)
                else :
                    yield scrapy.Request(detail, self.parse_now)
            rosters = []
            stats = []

    def parse_past(self, response):
        roster = pandas.read_html(response.url)[0]
        rosters.append(roster.to_dict())
