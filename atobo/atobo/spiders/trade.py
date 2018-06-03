# -*- coding: utf-8 -*-
import scrapy, re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.loader import ItemLoader
from atobo.items import AtoboItem

class TradeSpider(CrawlSpider):
    name = 'trade'
    # allowed_domains = ['www.atobo.com.cn']
    # 放置阿土伯索引连接
    start_urls = ['https://www.atobo.com.cn/']
    # 获取分类下的翻页
    rules = (
        Rule(LinkExtractor(allow='/Companys/s-c\d+/'), callback='parse', follow=True),
    )

    def parse(self, response):
        company_url = response.xpath('//li[@class="product_box"]').extract()
        for company in company_url:
            m = ItemLoader(item=JingdongItem(), response=response)
            # 使用add_xpath方法，传递Item类的字段名称和对应的xpath解析语法
            m.add_xpath('c_name', './/li[@class="pp_name"]/a/text()')
            m.add_xpath('c_url', './/li[@class="pp_name"]/a/@href')
            m.add_xpath('c_product', './/li[@class="pp_product"]/text()')
            m.add_xpath('c_address', './/li[@class="pp_address"]/strong/text()')
            return m.load_item
'''
            # c_name = company.xpath('.//li[@class="pp_name"]/a/text()').extract()
            # c_url = "https" + company.xpath('.//li[@class="pp_name"]/a/@href').extract()
            # c_product = company.xpath('.//li[@class="pp_product"]/text()').extract()
            # c_address = company.xpath('.//li[@class="pp_address"]/strong/text()').extract()
            # yield Request(url=c_url, callback=self.parse_company)


    def parse_company(self, response):
        l = ItemLoader(item=JingdongItem(), response=response)
        # 使用add_xpath方法，传递Item类的字段名称和对应的xpath解析语法
        l.add_xpath('shop_name', '//div[@class="product_name"]')
        l.add_xpath('goods_name', '//div[@class="product_title"]')
        l.add_xpath('normal_price', '//p[@id="price"]')
        l.add_xpath('now_price', '//p[@id="price"]')
        l.add_xpath('mon_sales', '//p[@id="price"]')
        l.add_xpath('total_views', '//p[@id="price"]')
        l.add_xpath('stock', '//p[@id="price"]')
        l.add_xpath('brand', '//p[@id="price"]')
        l.add_xpath('delivery_port', 'p#stock]')
        l.add_xpath('platform', 'today')
        return l.load_item

    def parse_business(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        # 详情页抽取数据
        m = ItemLoader(item=JingdongItem(), response=response)
        # 使用add_xpath方法，传递Item类的字段名称和对应的xpath解析语法
        m.add_xpath('shop_name', '//div[@class="product_name"]')
        m.add_xpath('goods_name', '//div[@class="product_title"]')
        m.add_xpath('normal_price', '//p[@id="price"]')
        m.add_xpath('now_price', '//p[@id="price"]')
        m.add_xpath('mon_sales', '//p[@id="price"]')
        m.add_xpath('total_views', '//p[@id="price"]')
        m.add_xpath('stock', '//p[@id="price"]')
        m.add_xpath('brand', '//p[@id="price"]')
        m.add_xpath('delivery_port', 'p#stock]')
        m.add_xpath('platform', 'today')
        return m.load_item

'''