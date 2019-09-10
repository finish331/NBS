# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NbsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # id = scrapy.Field()
    # number = scrapy.Field()
    # team = scrapy.Field()
    # position = scrapy.Field()
    # data = scrapy.Field()
    pass

class TeamItem(scrapy.Item):
    team = scrapy.Field()
    year = scrapy.Field()
    rosters = scrapy.Field()
    stats = scrapy.Field()
    # pass
