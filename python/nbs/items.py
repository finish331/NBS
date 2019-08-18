# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NbsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NbsItem(scrapy.Item):
    # define the fields for your item here like:
    number = scrapy.Field()
    name = scrapy.Field()
    position = scrapy.Field()
    team = scrapy.Field()
    game = scrapy.Field()
    points = scrapy.Field()
    rebounds = scrapy.Field()
    assists = scrapy.Field()
    FG = scrapy.Field()
    FG3 = scrapy.Field()
    FT = scrapy.Field()
    eFG = scrapy.Field()
    PER = scrapy.Field()
    WS = scrapy.Field()
    # pass
