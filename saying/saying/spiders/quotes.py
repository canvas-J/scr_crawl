# -*- coding: utf-8 -*-
import re
import scrapy
from saying.items import SayingItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['juzimi.com']
    # start_urls = ['http://www.juzimi.com/']
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',\
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',\
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'
    }

    def start_requests(self):
        urls = ['http://www.juzimi.com/article/'
        ]
        for url in urls:
            url = url + '百年孤独'
            yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        # 区域内查找使用相对路径，否则会重复查询
        for info in response.xpath('//div[contains(@class, "views-row views-row-")]'):
            item = SayingItem()
            cont = info.xpath('./div/div[1]/a/text()').extract() 
            content = re.sub(r'\\n', "", str(cont)).strip()
            item['content'] = content
            item['fancy'] = info.xpath('./div/div[3]/a/text()').extract()
            yield item

        next_page = response.xpath('//li[contains(@class, "pager-current")]/following-sibling::li[1]/a/@href').extract_first()
        if next_page is not None:
            next_page = 'http://www.juzimi.com' + next_page
            yield response.follow(next_page, headers=self.headers, callback=self.parse)