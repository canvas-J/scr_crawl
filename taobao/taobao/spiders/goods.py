# -*- coding: utf-8 -*-

from scrapy import Spider,Request
from selenium import webdriver
from taobao.items import TaobaoItem

class GoodsSpider(Spider):
    name = 'goods'

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(30)

    def closed(self,spider):
        print("spider closed")
        self.browser.close()

    def start_requests(self):
        start_urls = ['https://www.taobao.com/']
        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        selector = response.xpath('//div[contains(@class, "item J_MouserOnverReq")]/div/div/a/@href').extract()
        for url in selector:
            item = TaobaoItem()
            url = "http:" + url
            item['url'] = url
            # url = "http" + url[2:]
        # 关键是这里必须要有下一页的链接请求给中间件处理，但淘宝的下一页如何处理是个难题
        # 看能否在中间件改成生成器试试
        # next_pages = response.xpath('//li[@class="item active"]/following-sibling::li[1]/a/@href').extract()
        # for next_page in next_pages:
        #     url = "http:" + next_page
        #     print(url)
        #     yield Request(url=url, callback=self.parse)
