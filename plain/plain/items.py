# -*- coding: utf-8 -*-
from scrapy import Item, Field
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def strip_name(value):
    try:
        goods_name = value.replace(" ", "").replace("\n", "")
    except:
        goods_name = value.strip()
    return goods_name

class PlainItem(Item):
    area_index = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    search_name = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    total = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    num = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    location_lat = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    location_lng = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    province = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    city = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    street_id = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    telephone = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    detail = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    uid = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    url = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    name = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    address = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    build_year = Field(
        input_processor = MapCompose(strip_name),
        output_processor = Join(),
    )
    buildings = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    familys = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
    )
    area = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst(),
    )
    subway = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst(),
    )
    price = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst(),
    )
    estate = Field(
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


