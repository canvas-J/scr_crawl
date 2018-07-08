# -*- coding: utf-8 -*-
from selenium import webdriver
from scrapy import Spider,Request
from fake_useragent import UserAgent
from jingdong.items import JingdongItem
from scrapy.contrib.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor

class JdgoodsSpider(Spider):

    name = 'jdgoods'

    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument('headless')
        opt.add_argument('disable-gpu')
        opt.add_argument('useragent="{}"'.format(UserAgent().random))
        self.browser = webdriver.Chrome(chrome_options=opt)
        self.browser.set_page_load_timeout(30)

    def closed(self,spider):
        print("spider closed")
        self.browser.close()

    def start_requests(self):
        urls = []
        keyword = input("请输入你要爬取的关键词\t")
        pages = input("请输入你要爬取的页数\t")
        # keyword = self.settings.get('KEYWORD')
        for i in range(pages):
            urls.append('https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={}&psort=3&cid2=653&cid3=655&page={}&s={}&click=0'.format(keyword, keyword, 2*i+1, 60*i+1))
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        # 解析出详情页链接
        page_links = response.xpath('//li[@class="gl-item"]/div/div[@class="p-img"]/a').extract()
        for link in page_links:
            yield Request(url=link, callback=self.parse_item)

    def parse_item(self, response):
        # 详情页抽取数据
        l = ItemLoader(item=JingdongItem(), response=response)
        # 使用add_xpath方法，传递Item类的字段名称和对应的xpath解析语法
        l.add_xpath('shop_name', '//div[@id="popbox"]/div/div[1]/h3/a/text()')
        l.add_xpath('goods_name', '//div[@class="sku-name"]/text()')
        l.add_xpath('normal_price', '//div[@class="summary-price-wrap"]/div[1]/div[2]/span/span[2]/text()')

        l.add_xpath('now_price', '//p[@id="price"]')
        l.add_xpath('mon_sales', '//p[@id="price"]')

        l.add_xpath('total_views', '//div[@id="comment-count"]/a/text()')

        l.add_xpath('stock', '//p[@id="price"]')

        l.add_xpath('brand', '//ul[@id="parameter-brand"]/li/a/text()')

        l.add_xpath('delivery_port', 'p#stock]')
        l.add_xpath('platform', 'today')
        return l.load_item

