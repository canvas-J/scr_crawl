# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from fake_useragent import UserAgent
from huazhuangpin.items import HuazhuangpinItem


class BrandsSpider(scrapy.Spider):
    name = 'brands'
    allowed_domains = ['www.bevol.cn']
    start_urls = []
    brands_file = open('brands.txt')
    brands_list = brands_file.readlines()
    for dex in brands_list:
        start_urls.append('https://www.bevol.cn/product?keywords={}'.format(dex))

    def parse(self, response):
        if response.status==200:
            for information in response.xpath('//div[@class="goods-main-info-box"]/ul[@class="page-content"]/a'):
                item = HuazhuangpinItem()
                item['url'] = "https://www.bevol.cn" + information.xpath('./@href').extract_first()
                item['category'] = response.url[38:]
                yield item
            if '&p=' not in response.url:
                total_page = response.xpath('//div[@class="foot-page"]/div[@class="tcdPageCode"]/a[@class="tcdNumber"]/text()').extract()
                print(total_page[-1])
                for page in range(2, int(total_page[-1])+1):
                    url = response.url + "&p={}".format(page)
                    yield scrapy.Request(url=url, callback=self.parse)

        elif response.status==202:
            yield scrapy.Request(response.url, callback=self.parse, dont_filter=True)
