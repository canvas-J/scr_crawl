# -*- coding: utf-8 -*-
import pandas as pd
from scrapy import Spider,Request
from plain.items import PlainItem
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor

class PlainSpider(Spider):

    name = 'wiwj'
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["url", "name", "address", "build_year", "buildings", "familys", "area", "subway", "price", "estate"],
        }

    def start_requests(self):
        for num in range(1, 556):
            yield Request(url="https://sh.5i5j.com/xiaoqu/n{}/".format(num), callback=self.parse)

    def parse(self, response):
        messages = response.xpath('//div[@class="lfBox lf"]/div/ul/li/div[@class="listCon"]')
        for mes in messages:
            page_link = "https://sh.5i5j.com" + mes.xpath('.//h3/a/@href').extract_first()
            subway = mes.xpath('.//div/p[last()]/text()')
            yield Request(url=page_link, callback=self.parse_item, meta={'subway':subway,})

    def parse_item(self, response):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        l = ItemLoader(item=PlainItem(), response=response)
        l.add_value('url', response.url)
        try:
            l.add_xpath('name', '/html/body/div[3]/div[1]/div[1]/h1/text()')
        except:
            l.add_value('name', '')

        try:
            l.add_xpath('address', '/html/body/div[3]/div[1]/div[1]/p/text()')
        except:
            l.add_value('address', '')

        try:
            l.add_xpath('build_year', '//div[@class="content fr"]/div[@class="xqfangs"]/ul/li[1]/text()')
        except:
            l.add_value('build_year', '')

        try:
            l.add_xpath('buildings', '//div[@class="content fr"]/div[@class="xqfangs"]/ul/li[2]/text()')
        except:
            l.add_value('buildings', '')

        try:
            l.add_xpath('familys', '//div[@class="content fr"]/div[@class="xqfangs"]/ul/li[3]/text()')
        except:
            l.add_value('familys', '')

        try:
            l.add_xpath('area', '/html/body/div[2]/div/div[1]/a[3]/text()')
        except:
            l.add_value('area', '')
            
        try:
            l.add_value('subway', response.meta['subway'])
        except:
            l.add_value('subway', '')

        try:
            l.add_xpath('price', '//div[@class="content fr"]/div[1]/span/text()')
        except:
            l.add_value('price', '')

        try:
            l.add_xpath('estate', '//div[@class="xqsaleinfo"]/ul/li[2]/em/text()')
        except:
            l.add_value('estate', '')

        # try:
        #     details = response.xpath('//div[@class="p-parameter"]/ul[2]/*/text()').extract()
        #     for i in range(len(details)):
        #         l.add_value('item{}'.format(i), details[i])
        # except:
        #     for i in range(9):
        #         l.add_value('item{}'.format(i), '')
        yield l.load_item()
