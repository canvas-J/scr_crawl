# -*- coding: utf-8 -*-

from scrapy import Spider,Request
from selenium import webdriver
from taobao.items import TaobaoItem

class GoodsSpider(Spider):

    name = 'goods'

    # def __init__(self):
    #     opt = webdriver.ChromeOptions()
    #     opt.add_argument('headless')
    #     opt.add_argument('disable-gpu')
    #     opt.add_argument('useragent="{}"'.format(UserAgent().random))
    #     self.browser = webdriver.Chrome(chrome_options=opt)
    #     self.browser.set_page_load_timeout(30)

    # def closed(self,spider):
    #     print("spider closed")
    #     self.browser.close()
        
    def start_requests(self):
        start_urls = ['https://detail.tmall.hk/hk/item.htm?spm=a1z10.3-b-s.w4011-15152802804.138.30f843ebhrkcHR&id=540780745071&rn=42b5220dd0858d6f44c7cf3c9bbabd89&abbucket=4.com']
        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status==200:
            selector = response.xpath('/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[1]/h1').extract()
            item = TaobaoItem()
            item['url'] = selector
        elif response.status==202:
            yield Request(response.url, callback=self.parse, dont_filter=True)
