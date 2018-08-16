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

class AtobodetailItem(Item):
    c_name = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    url = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    category = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    hangye = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    quxian = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    ximu = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    mingcheng = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    zhuangtai = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    zhucehao = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    farendaibiao = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    zhuceziben = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    qiyeleixing = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    dengjijiguan = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    chengliriqi = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    yingyeqixian = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    jingyingfanwei = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    zhucedizhi = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    gaoguan1 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    zhiwei1 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    gaoguan2 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    zhiwei2 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    gaoguan3 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    zhiwei3 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    gaoguan4 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    zhiwei4 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    gudong1 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    renjiao1 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    shijiao1 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    chigubili1 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    gudong2 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    renjiao2 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    shijiao2 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    chigubili2 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    gudong3 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    renjiao3 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    shijiao3 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    chigubili3 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    duiwaitouzi = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    wangdian1 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    lianxiren1 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    lianxidianhua1 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    shouji1 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    zhuyingchanpin1 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    wangdian2 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    lianxiren2 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    lianxidianhua2 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    shouji2 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )
    zhuyingchanpin2 = Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(),
        )