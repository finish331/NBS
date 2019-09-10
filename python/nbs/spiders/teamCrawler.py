import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup as BS
from NBS.items import TeamItem
import pandas
import requests


class TeamCrawler(CrawlSpider):
    name = 'teamCrawler'
    start_urls = ['https://www.basketball-reference.com/teams/']

    def parse(self, response):
        url = 'https://www.basketball-reference.com'
        res = BS(response.body, 'lxml')
        table = res.select('table')[0]
        links = table.select('a')
        # for link in links:
        #     teamItem = TeamItem()
        #     for year in range(2010 ,2021):
        #         detail = url + link.get('href') + str(year) + '.html'
        #         yield scrapy.Request(detail, self.parse_detail, meta={'year': str(year)})
        #     teamItem['name'] = link.text
        #     teamItem['rosters'] = rosters
        #     teamItem['stats'] = stats
        team = {
            "year": [],
            "rosters": [],
            "stats": []
        }
        for year in range(2017, 2021):
            detail = 'https://www.basketball-reference.com/teams/BOS/' + \
                str(year) + '.html'
            team["year"].append(year)
            yield scrapy.Request(url=detail, meta={"item": team}, callback=self.parse_detail)
            print(team)
        print(team)
        # teamItem = TeamItem()
        # teamItem["team"] = "BOS"
        # teamItem["year"] = []
        # teamItem["rosters"] = []
        # teamItem["stats"] = []
        # teamItem["year"] = team["year"]
        # teamItem["rosters"] = team["rosters"]
        # teamItem["stats"] = team["stats"]
        # return teamItem

    def parse_detail(self, response):
        item = response.meta["item"]
        # 取得球員名單
        roster = pandas.read_html(response.url)[0]
        item["rosters"].append(roster.to_dict())
        # 取得球隊資料
        html = requests.get(response.url).text
        soup = BS(html, 'html.parser')
        placeholders = soup.find_all('div', {'class': 'placeholder'})
        table = None
        for title in placeholders:
            # get elements after placeholder and join in one string
            comment = ''.join(title.next_siblings)
            # parse comment
            soup_comment = BS(comment, 'html.parser')
            if soup_comment.find(id='team_and_opponent') != None:
                table = soup_comment.find(id='team_and_opponent')
                data = pandas.read_html(str(table))[0]
                item["stats"].append(data.to_dict())
                break
        if table == None:
            item["stats"].append(table)
        return item
