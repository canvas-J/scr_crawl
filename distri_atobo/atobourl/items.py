# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AtobourlItem(scrapy.Item):
    # define the fields for your item here like:
    category = scrapy.Field()
    co_links = scrapy.Field()
    bu_links = scrapy.Field()
    c_name = scrapy.Field()
    c_product = scrapy.Field()
    c_address = scrapy.Field()
    quxian = scrapy.Field()
    hangye = scrapy.Field()
    ximu = scrapy.Field()