# -*- coding: utf-8 -*-
import pandas as pd
from scrapy import Spider,Request
from plain.items import PlainItem
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor

class PlainSpider(Spider):

    name = 'lianjia'
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["url", "name", "address", "build_year", "buildings", "familys", "area", "subway", "price", "estate"],
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.area_links = pd.DataFrame(pd.read_excel('L-url.xlsx',encoding='gb18030'))

    def start_requests(self):
        urls = list(self.area_links.ix[:, 0])
        # urls = ['https://sh.lianjia.com/xiaoqu/beicai']
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        messages = response.xpath('//div[@class="leftContent"]/ul/li/div[@class="info"]')
        for mes in messages:
            page_link = mes.xpath('.//div[@class="title"]/a/@href').extract_first()
            subway = mes.xpath('.//div[last()]/span/text()').extract_first()
            yield Request(url=page_link, callback=self.parse_item, meta={'subway':subway,})
        if "/pg" not in str(response.url):
            for num in range(2, 31):
                yield Request(url="{}pg{}/".format(response.url,num), callback=self.parse)

    def parse_item(self, response):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        l = ItemLoader(item=PlainItem(), response=response)
        l.add_value('url', response.url)
        try:
            l.add_xpath('name', '/html/body/div[4]/div/div[1]/h1/text()')
        except:
            l.add_value('name', '')

        try:
            l.add_xpath('address', '/html/body/div[4]/div/div[1]/div/text()')
        except:
            l.add_value('address', '')

        try:
            l.add_xpath('build_year', '/html/body/div[6]/div[2]/div[2]/div[1]/span[2]/text()')
        except:
            l.add_value('build_year', '')

        try:
            l.add_xpath('buildings', '/html/body/div[6]/div[2]/div[2]/div[6]/span[2]/text()')
        except:
            l.add_value('buildings', '')

        try:
            l.add_xpath('familys', '/html/body/div[6]/div[2]/div[2]/div[7]/span[2]/text()')
        except:
            l.add_value('familys', '')

        try:
            l.add_xpath('area', '/html/body/div[5]/div[1]/a[3]/text()')
        except:
            l.add_value('area', '')
            
        try:
            l.add_value('subway', response.meta['subway'])
        except:
            l.add_value('subway', '')

        try:
            l.add_xpath('price', '/html/body/div[6]/div[2]/div[1]/div/span[1]/text()')
        except:
            l.add_value('price', '')

        try:
            l.add_xpath('estate', '/html/body/div[6]/div[2]/div[2]/div[4]/span[2]/text()')
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
