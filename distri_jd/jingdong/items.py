# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def strip_name(value):
    try:
        goods_name = value.replace(" ", "").replace("\n", "")
    except:
        goods_name = value.strip()

    return goods_name

class JingdongItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cate_key = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    goods_url = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    platform = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    shop_name = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    goods_name = Field(
        input_processor = MapCompose(strip_name),
        output_processor = Join(),
    )
    now_price = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    origin_price = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    # now_price = Field()
    # mon_sales = Field()
    total_views = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    # stock = Field()
    brand = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst(),
    )
    item0 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item1 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item2 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item3 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item4 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item5 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item6 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item7 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item8 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item9 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item10 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item11 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item12 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item13 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item14 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item15 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    item16 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    ) 