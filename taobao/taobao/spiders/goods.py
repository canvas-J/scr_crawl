# -*- coding: utf-8 -*-

from scrapy import Spider,Request
from selenium import webdriver

class GoodsSpider(Spider):
    name = 'goods'

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(30)

    def closed(self,spider):
        print("spider closed")
        self.browser.close()

    def start_requests(self):
        start_urls = ['https://s.taobao.com/search?q=%E7%94%B7%E5%A3%AB%E7%88%BD%E8%82%A4%E6%B0%B4&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306']
        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        selector = response.xpath('//div[contains(@class, "item J_MouserOnverReq")]/div/div/a/@href').extract()
        print(len(selector))
        print('---------------------------------------------------')
        print(selector[0])