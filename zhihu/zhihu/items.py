# -*- coding: utf-8 -*-
import scrapy

class ZhihuItem(scrapy.Item):
    que_name = scrapy.Field()
    link = scrapy.Field()
    user_id = scrapy.Field()
    user_link = scrapy.Field()
    praise = scrapy.Field()
    comments = scrapy.Field()
    article = scrapy.Field()
    pub_time = scrapy.Field()
    edit_time = scrapy.Field()
