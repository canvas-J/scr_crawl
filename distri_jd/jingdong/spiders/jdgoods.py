# -*- coding: utf-8 -*-
import re
from selenium import webdriver
from scrapy import Request
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from jingdong.items import JingdongItem
from scrapy.loader import ItemLoader
from scrapy_redis.spiders import RedisSpider
from scrapy.linkextractors import LinkExtractor

class JdgoodsSpider(RedisSpider):

    name = 'jdgoods'
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ['cate_key', 'goods_url', "platform", "shop_name", "goods_name", "now_price", "origin_price", "total_view", "brand", "item0", "item1", "item2", "item3", "item4", "item5", "item6", "item7", "item8", "item9", "item10", "item11", "item12", "item13", "item14", "item15", "item16"],
        }
    redis_key = "clinks:start_urls" # https://www.atobo.com.cn/Companys

    def parse(self, response):
        urls = []
        keywords = self.settings.get('KEYWORDS')
        pages = self.settings.get('MAX_PAGE')
        for keyword in keywords:
            for i in range(int(pages)):
                urls.append('https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={}&psort=3&stock=1&page={}&s={}&click=0'.format(keyword, keyword, 2*i+1, 60*i+1))
        for url in urls:
            cate_key = re.match('keyword=(.*?)&enc=', url)
            print(cate_key)
            yield Request(url=url, callback=self.parse_link, meta={'cate_key': cate_key,})

    def parse_link(self, response):
        # 解析出详情页链接
        if response.status==200:
            page_links = response.xpath('//li[@class="gl-item"]/div/div[@class="p-img"]/a/@href').extract()
            cate_key = response.meta['cate_key']
            for link in page_links:
                link = "https:" + link
                yield Request(url=link, callback=self.parse_item, meta={'cate_key': cate_key,})
        elif response.status==202:
            cate_key = response.meta['cate_key']
            yield Request(response.url, callback=self.parse_link, dont_filter=True, meta={'cate_key': cate_key,})

    def parse_item(self, response):
        if response.status==200:
            soup = bs(response.text, "lxml")
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            # 详情页抽取数据
            l = ItemLoader(item=JingdongItem(), response=response)
            # 使用add_xpath方法，传递Item类的字段名称和对应的xpath解析语法
            l.add_value('cate_key', response.meta['cate_key'])
            l.add_value('goods_url', response.url)
            try:
                l.add_xpath('platform', '//div[@id="logo-2014"]/a/text()')
            except:
                l.add_value('platform', '')

            try:
                l.add_xpath('shop_name', '//div[@id="popbox"]/div/div[1]/h3/a/text()')
            except:
                l.add_value('shop_name', '')

            try:
                l.add_xpath('goods_name', '//div[@class="sku-name"]/text()')
            except:
                l.add_value('goods_name', '')

            try:
                l.add_xpath('now_price', '//div[@class="summary-price-wrap"]/div[1]/div[2]/span/span[2]/text()')
            except:
                l.add_value('now_price', '')

            try:
                l.add_xpath('origin_price', '//*[@id="page_origin_price"]/text()')
            except:
                l.add_value('origin_price', '')

            # try:
        #         l.add_xpath('mon_sales', '//p[@id="price"]')
            # except:
            #     l.add_value('mon_sales', '')

            try:
                l.add_xpath('total_views', '//div[@id="comment-count"]/a/text()')
            except:
                l.add_value('total_views', '')

            # try:
            #     l.add_xpath('stock', '//p[@id="price"]')
            # except:
            #     l.add_value('stock', '')

            try:
                l.add_xpath('brand', '//ul[@id="parameter-brand"]/li/a/text()')
            except:
                l.add_value('brand', '')

            try:
                details = soup.select('.p-parameter > ul[2] > li')
                for i in range(len(details)):
                    l.add_value('item{}'.format(i), details[i].string)
            except:
                for i in range(9):
                    l.add_value('item{}'.format(i), '')
            yield l.load_item()
        elif response.status==202:
            cate_key = response.meta['cate_key']
            yield Request(response.url, callback=self.parse_item, dont_filter=True, meta={'cate_key': cate_key,})
