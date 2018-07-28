# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuazhuangpinItem(scrapy.Item):
    url = scrapy.Field()
    # name = scrapy.Field()
    # e_name = scrapy.Field()
    # bieming = scrapy.Field()
    # beian = scrapy.Field()
    category = scrapy.Field()


