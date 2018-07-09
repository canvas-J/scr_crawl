# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class JingdongItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    platform = Field()
    shop_name = Field()
    goods_name = Field()
    normal_price = Field()
    # now_price = Field()
    # mon_sales = Field()
    total_views = Field()
    # stock = Field()
    brand = Field()
    item0 = Field()
    item1 = Field()
    item2 = Field()
    item3 = Field()
    item4 = Field()
    item5 = Field()
    item6 = Field()
    item7 = Field()
    item8 = Field()


