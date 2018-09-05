# -*- coding: utf-8 -*-
import pandas as pd
from scrapy import Spider,Request
from plain.items import PlainItem
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor

class PlainSpider(Spider):

    name = 'soufang'
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["url", "name", "address", "build_year", "buildings", "familys", "area", "subway", "price", "estate"],
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.area_links = pd.DataFrame(pd.read_excel('S-url.xlsx', encoding='gb18030'))

    def start_requests(self):
        # urls = list(self.area_links.ix[:, 0])
        urls = ['http://www.sofang.com/saleesb/area/aa2992']
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.text)
        messages = response.xpath('//div[@class="list list_free xinfang"]/dl/dd[@class="house_msg"]')
        for mes in messages:
            page_link = 'http://www.sofang.com' + mes.xpath('.//p/a/@href').extract_first()
            # subway = mes.xpath('.//div/p[last()]/span/a[2]/text()').extract_first()
            yield Request(url=page_link.replace('index','bd'), callback=self.parse_item)
        if "-bl" not in str(response.url):
            for num in range(2, 4):
                yield Request(url="{}-bl{}?".format(response.url,num), callback=self.parse)

    def parse_item(self, response):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        l = ItemLoader(item=PlainItem(), response=response)
        l.add_value('url', response.url)
        try:
            l.add_xpath('name', '/html/body/div[4]/div[1]/dl/dt/span[1]/text()')
        except:
            l.add_value('name', '')

        try:
            l.add_xpath('address', '/html/body/div[4]/div[3]/ul/li[last()]/span[2]/text()')
        except:
            l.add_value('address', '')

        try:
            l.add_xpath('build_year', '/html/body/div[4]/div[3]/ul/li[7]/span[2]/text()')
        except:
            l.add_value('build_year', '')

        try:
            l.add_xpath('buildings', '/html/body/div[4]/div[3]/ul/li[10]/span[2]/text()')
        except:
            l.add_value('buildings', '')

        try:
            l.add_xpath('familys', '/html/body/div[4]/div[3]/ul/li[12]/span[2]/text()')
        except:
            l.add_value('familys', '')

        try:
            l.add_xpath('area', '/html/body/div[4]/div[3]/ul/li[3]/span[2]/text()')
        except:
            l.add_value('area', '')
            
        try:
            l.add_value('subway', '/html/body/div[4]/div[3]/ul/li[5]/span[2]/text()')
        except:
            l.add_value('subway', '')

        try:
            l.add_xpath('price', '/html/body/div[4]/div[1]/dl/dd/p[2]/span[2]/span/text()')
        except:
            l.add_value('price', '')

        try:
            l.add_xpath('estate', '/html/body/div[4]/div[3]/ul/li[1]/span[2]/text()')
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
