# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from component.items import ComponentItem

class CompoSpider(scrapy.Spider):
    name = 'compo'
    allowed_domains = ['www.bevol.cn']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.all_links = pd.DataFrame(pd.read_csv('brands_all_data.csv'))

    def start_requests(self):
        urls = list(self.all_links.ix[:, "url"])
        for num, url in enumerate(urls):
            if "http" not in url:
                break
            category = str(self.all_links.iloc[num, 0])
            yield scrapy.Request(url=url, callback=self.parse, meta={'category': category})

    def parse(self, response):
        if response.status==200:
            item = ComponentItem()
            item['url'] = response.url
            item['category'] = response.meta['category'].strip()
            item['c_name'] = response.xpath('string(//div[@class="crumbs_nav"]/h2)').extract_first().split('/')[-1].strip()
            # item['c_name1'] = response.xpath('string(//*[@id="goods-info-html"]/div/h1)').extract_first()
            item['e_name'] = response.xpath('//div[@id="goods-info-html"]/div/p[@class="p2"]/text()').extract_first()
            item['o_name'] = response.xpath('//div[@id="goods-info-html"]/div/p[@class="p3"]/text()').extract_first()
            item['others'] = response.xpath('//div[@id="goods-info-html"]/div/p[@class="p4"]/text()').extract_first()
            item['beian'] = response.xpath('//div[@id="goods-info-html"]/div/p[@class="p5"]/text()').extract_first().strip()
            components = response.xpath('//div[contains(@class,"chengfenbiao")]/table[@class="table"]/tbody/tr/td/a/text()')
            for i in range(len(components)):
                item['c_{}'.format(i)] = components[i].extract()
            yield item       
        elif response.status==202:
            category = response.meta['category'].strip()
            yield scrapy.Request(response.url, callback=self.parse, dont_filter=True, meta={'category': category})


