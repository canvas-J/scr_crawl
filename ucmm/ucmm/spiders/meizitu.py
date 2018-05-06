# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ucmm.items import JiandanItem


class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    # allowed_domains = ['baidu.com']

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',\
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',\
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'
    }

    def start_requests(self):
        urls = ['http://www.ucmmw.com/',
            'http://www.ucmmw.com/xieetu',
            'http://www.ucmmw.com/zhainannvshen',
            'http://www.ucmmw.com/haohaizikanbujian']
        for url in urls:
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        imgs = response.xpath('//div[@class="thumbnail"]/a/img/@src').extract()
        # img_names = response.xpath('//div[@class="thumbnail"]/a/@title').extract()
        item = JiandanItem()
        item['image_urls'] = imgs
        # item['image_names'] = img_names
        yield item

        next_page = response.xpath('//a[@class="current"]/following-sibling::a[1]/@href').extract_first()
        if next_page is not None:
            # next_page = 'http:' + next_page
            yield scrapy.Request(next_page, headers=self.headers, callback=self.parse)

    # def parse(self, response):
    #     list_imgs = response.xpath('//div[@class="article"]/h2/a/@href').extract()
    #     for url in list_imgs:
    #         yield scrapy.Request(url, headers=self.headers, callback=self.parse_img)
    # def parse_img(self, response):
    #     imgs = response.xpath('//div[@id="post_content"]/p/img/@src').extract()
    #     item = JiandanItem()
    #     item['image_urls'] = imgs
    #     yield item