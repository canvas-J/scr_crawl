# -*- coding: utf-8 -*-

import scrapy


class ReviewItem(scrapy.Item):
    # define the fields for your item here like:
    rate_id = scrapy.Field()
    guige = scrapy.Field()
    pinglun = scrapy.Field()
    yonghuming = scrapy.Field()
    shijian1 = scrapy.Field()
    shijian2 = scrapy.Field()
    zhuiping = scrapy.Field()

