# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.loader import ItemLoader
from jingdong.items import JingdongItem

class JdgoodsSpider(scrapy.Spider):
    name = 'jdgoods'
    # allowed_domains = ['www.jd.com']
    start_urls = ['http://www.jd.com/']

    def parse(self, response):
        # 解析出详情页链接
        selector = response.xpath('').extract()
        for url in selector:
            yield Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        # 详情页抽取数据
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

