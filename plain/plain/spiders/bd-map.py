# -*- coding: utf-8 -*-
import pandas as pd
import scrapy, json, re
from plain.items import PlainItem

class MapSpider(scrapy.Spider):
    name = 'bd-map'
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["search_name", "num", "name", "location_lat", "location_lng", "address", 
                    "province", "city", "area", "street_id", "telephone", "detail", "uid"],
        }
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.df = pd.DataFrame(pd.read_excel('lianjia.xlsx',encoding='gb18030'))

    def start_requests(self):
        names = list(self.df.ix[:, '小区名'])
        areas = ['上海']
        aks = ['zqSxjTdW45ZIz1doqSFxg75exTKVbvGM', 'uf2tGOWmZnAVZ8bK2tA1WGmEVRu98rtO']
        for area in areas:
            for name in names:
                api = 'http://api.map.baidu.com/place/v2/search?query={}&region={}&output=json&ak={}'.format(name, area, aks[0])
                yield scrapy.Request(url=api, callback=self.parse, meta={'name': name})

    def parse(self, response):
        obj_json = json.loads(response.text)
        data_list = obj_json["results"]
        for num, message in enumerate(data_list):
            item = PlainItem()
            item["search_name"] = response.meta['name']
            item['num'] = num + 1
            item['name'] = message['name']
            item['location_lat'] = message['location']['lat']
            item['location_lng'] = message['location']['lng']
            item['address'] = message['address']
            try:
                item['province'] = message['province']
            except:
                item['province'] = ""
            try:
                item['city'] = message['city']
            except:
                item['city'] = ""
            try:
                item['area'] = message['area']
            except:
                item['area'] = ""
            try:
                item['street_id'] = message['street_id']
            except:
                item['street_id'] = ""
            try:
                item['telephone'] = message['telephone']
            except:
                item['telephone'] = ""
            try:
                item['detail'] = message['detail']
            except:
                item['detail'] = ""
            try:
                item['uid'] = message['uid']
            except:
                item['uid'] = ""
            yield item
