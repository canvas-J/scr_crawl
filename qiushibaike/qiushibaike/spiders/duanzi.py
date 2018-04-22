# -*- coding: utf-8 -*-
import re
import scrapy
from qiushibaike.items import QiushibaikeItem

class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['https://qiushibaike.com/']
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',\
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',\
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'
    }

    def start_requests(self):
        urls = ['https://qiushibaike.com/',
        'https://www.qiushibaike.com/hot/',
        'https://www.qiushibaike.com/textnew/',
        'https://www.qiushibaike.com/history/',
        'https://www.qiushibaike.com/text/'
        ]
        for url in urls:
            yield scrapy.Request(url, headers=self.headers)
    
    def parse(self, response):
        # 区域内查找使用相对路径，否则会重复查询
        for info in response.xpath('//div[contains(@class, "article block untagged mb15")]'):
            item = QiushibaikeItem()
            content = info.xpath('./a/div/span/text()').extract()
            author = info.xpath('./div/a[2]/h2/text()').extract()
            rep = re.compile(r'\\n') 
            content = re.sub(rep, "", str(content)).strip()
            author = re.sub(rep, "", str(author)).strip()
            item['content'] = content
            item['author'] = author
            item['fancy'] = info.xpath('./div/span/i/text()').extract()
            item['comment'] = info.xpath('./div/span/a/i/text()').extract()
            yield item


        next_page = response.xpath('//span[@class="current"]/../following-sibling::li[1]/a/@href').extract_first()
        if next_page is not None:
            # next_page = 'http:' + next_page
            yield response.follow(next_page, headers=self.headers, callback=self.parse)