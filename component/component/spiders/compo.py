# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from component.items import ComponentItem

class CompoSpider(scrapy.Spider):
    name = 'compo'
    allowed_domains = ['www.bevol.cn']
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["url", "category", "c_name", "e_name", "o_name", "beian", 
        "c_0", "c_1", "c_2", "c_3", "c_4", "c_5", "c_6", "c_7", "c_8", "c_9", "c_10", 
        "c_11", "c_12", "c_13", "c_14", "c_15", "c_16", "c_17", "c_18", "c_19", "c_20", 
        "c_21", "c_22", "c_23", "c_24", "c_25", "c_26", "c_27", "c_28", "c_29", "c_30", 
        "c_31", "c_32", "c_33", "c_34", "c_35", "c_36", "c_37", "c_38", "c_39", "c_40", 
        "c_41", "c_42", "c_43", "c_44", "c_45", "c_46", "c_47", "c_48", "c_49", "c_50", 
        "c_51", "c_52", "c_53", "c_54", "c_55", "c_56", "c_57", "c_58", "c_59", "c_60", 
        "c_61"],
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.all_links = pd.DataFrame(pd.read_csv('brands_all_data.csv', encoding='gb18030'))

    def start_requests(self):
        urls = list(self.all_links.ix[:, "url"])
        for num, url in enumerate(urls):
            if "http" not in url:
                break
            category = str(self.all_links.iloc[num, 1])
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


