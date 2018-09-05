# -*- coding: utf-8 -*-
import pandas as pd
from scrapy import Spider,Request
from plain.items import PlainItem
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor

class PlainSpider(Spider):

    name = 'ftx01'
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["url", "name", "area", "price", "item0", "item1", "item2", "item3", "item4",
        "item5", "item6", "item7", "item8", "item9", "item10"],
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.area_links = pd.DataFrame(pd.read_excel('F-url.xlsx', encoding='gb18030'))

    def start_requests(self):
        urls = list(self.area_links.ix[:, 0])
        # urls = ['https://sh.esf.fang.com/housing/25_1646_0_0_0_0_1_0_0_0/']
        for url in urls:
            yield Request(url=str(url), callback=self.parse)

    def parse(self, response):
        page_num = response.xpath('/html/body/div[4]/div[5]/ul/li[3]/span/span/text()').extract_first().split('/')[-1]
        messages = response.xpath('//div[@class="houseList"]/div/dl/dd')
        for mes in messages:
            page_link = mes.xpath('.//p[1]/a/@href').extract_first()
            # subway = mes.xpath('.//div[last()]/span/text()').extract_first()
            yield Request(url=page_link, callback=self.parse_item)
        if int(page_num) > 1 and response.url[-9:-1] == '_1_0_0_0':
            for num in range(2, int(page_num)+1):
                yield Request(url="{}_{}_0_0_0/".format(response.url[:-9],num), callback=self.parse)

    def parse_item(self, response):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        l = ItemLoader(item=PlainItem(), response=response)
        l.add_value('url', response.url)
        try:
            l.add_xpath('name', '/html/body/div[5]/div[2]/div[1]/h1/strong/text()')
        except:
            l.add_value('name', '')

        try:
            l.add_xpath('area', '/html/body/div[3]/div/div[2]/a[4]/text()')
        except:
            l.add_value('area', '')

        try:
            l.add_xpath('price', '/html/body/div[5]/div[2]/div[2]/span[1]/text()')
        except:
            l.add_value('price', '')

        try:
            details = response.xpath('//div[@class="firstright"]/div[@class="Rinfolist"]/ul/li')
            for i in range(len(details)):
                l.add_value('item{}'.format(i), details[i].xpath('string(.)').extract_first())
        except:
            for i in range(9):
                l.add_value('item{}'.format(i), '')
        yield l.load_item()
