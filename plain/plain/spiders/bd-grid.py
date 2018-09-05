# -*- coding: utf-8 -*-
import pandas as pd
import scrapy, json, re
from plain.items import PlainItem

class GridSpider(scrapy.Spider):
    name = 'bd-grid'
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["url", "area_index", "total", "num", "name", "location_lat", "location_lng", "address", 
                    "province", "city", "area", "street_id", "telephone", "detail", "uid"],
        }
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loc = ['30.67594', '120.90348', '31.31831', '122.00790', '31.30252', '121.13403', '31.85380', '121.98950']
        # loc = ['31.2273', '121.4508', '31.2773', '121.5008', '31.3485', '121.4278', '31.3985', '121.4778']
        dist_a = [float(loc[2])-float(loc[0]), float(loc[3])-float(loc[1])]
        dist_b = [float(loc[6])-float(loc[4]), float(loc[7])-float(loc[5])]
        lat_a = [x/100.0 + float(loc[0]) for x in range(int(dist_a[0]*100))]
        lng_a = [x/100.0 + float(loc[1]) for x in range(int(dist_a[1]*100))]
        lat_b = [x/100.0 + float(loc[4]) for x in range(int(dist_b[0]*100))]
        lng_b = [x/100.0 + float(loc[5]) for x in range(int(dist_b[1]*100))]
        self.coo_a = [[x, y] for x in lat_a for y in lng_a]
        self.coo_b = [[x, y] for x in lat_b for y in lng_b]

    def start_requests(self):
        aks = ['zqSxjTdW45ZIz1doqSFxg75exTKVbvGM', 'uf2tGOWmZnAVZ8bK2tA1WGmEVRu98rtO']
        for index, point in enumerate(self.coo_a):
            api = 'http://api.map.baidu.com/place/v2/search?query=小区&bounds={},{},{},{}&page_size=20&page_num=0&output=json&ak={}'.format(point[0], point[1], point[0]+0.01, point[1]+0.01, aks[1])
            yield scrapy.Request(url=api, callback=self.parse, meta={'index': index+10000, 'page_num': 0})
        # for index, point in enumerate(self.coo_b):
        #     api = 'http://api.map.baidu.com/place/v2/search?query=小区&bounds={},{},{},{}&page_size=20&page_num=0&output=json&ak={}'.format(point[0], point[1], point[0]+0.01, point[1]+0.01, aks[1])
        #     yield scrapy.Request(url=api, callback=self.parse, meta={'index': index+20000, 'page_num': 0})

    def parse(self, response):
        obj_json = json.loads(response.text)
        index = response.meta['index']
        page_num = response.meta['page_num']
        if 'page_num=0' in response.url:
            number = obj_json["total"]
            if number%20 == 0:
                pages = number/20
            else:
                pages = number//20 + 1
            if pages > 1:
                for n in range(1, pages):
                    url = response.url.replace('page_num=0', 'page_num={}'.format(n))
                    yield scrapy.Request(url=url, callback=self.parse, meta={'index': index, 'page_num': n})
        data_list = obj_json["results"]
        if len(data_list) > 0:
            total = obj_json["total"]
            for num, message in enumerate(data_list):
                item = PlainItem()
                item['url'] = response.url
                item["area_index"] = index + 1
                item["total"] = total
                item['num'] = page_num*20 + num + 1
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
