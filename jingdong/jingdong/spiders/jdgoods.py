# -*- coding: utf-8 -*-
from selenium import webdriver
from scrapy import Spider,Request
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from jingdong.items import JingdongItem
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor

class JdgoodsSpider(Spider):

    name = 'jdgoods'

    def __init__(self):
        opt = webdriver.ChromeOptions()
        # opt.add_argument('headless')
        opt.add_argument('disable-gpu')
        opt.add_argument('useragent="{}"'.format(UserAgent().random))
        self.browser = webdriver.Chrome(chrome_options=opt)
        self.browser.set_page_load_timeout(30)

    def closed(self,spider):
        print("spider closed")
        self.browser.close()

    def isExist(self, rule, soup):
        try:
            soup.select_one(rule)
            return True
        except:
            return False

    def start_requests(self):
        urls = []
        keyword = input("请输入你要爬取的关键词\t")
        pages = input("请输入你要爬取的页数\t")
        # keyword = self.settings.get('KEYWORD')
        for i in range(int(pages)):
            urls.append('https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={}&psort=3&cid2=653&cid3=655&page={}&s={}&click=0'.format(keyword, keyword, 2*i+1, 60*i+1))
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        # 解析出详情页链接
        page_links = response.xpath('//li[@class="gl-item"]/div/div[@class="p-img"]/a/@href').extract()
        for link in page_links:
            link = "https:" + link
            yield Request(url=link, callback=self.parse_item)

    def parse_item(self, response):
        soup = bs(response, "lxml")
        # 详情页抽取数据
        print(soup.select_one('#popbox > div > div > h3 > a'))
        i = input()
        l = ItemLoader(item=JingdongItem(), response=response)
        # 使用add_xpath方法，传递Item类的字段名称和对应的xpath解析语法
        if self.isExist('#popbox > div > div > h3 > a', soup):
            l.add_xpath('platform', '//div[@id="logo-2014"]/a/text()')
        else:
            l.add_value('platform', '')

        if self.isExist('#popbox > div > div > h3 > a', soup):
            l.add_xpath('shop_name', '//div[@id="popbox"]/div/div[1]/h3/a/text()')
        else:
            l.add_value('shop_name', '')

        if self.isExist('.sku-name', soup):
            l.add_xpath('goods_name', '//div[@class="sku-name"]/text()')
        else:
            l.add_value('goods_name', '')

        if self.isExist('.summary-price-wrap > div > div > span > span', soup):
            l.add_xpath('normal_price', '//div[@class="summary-price-wrap"]/div[1]/div[2]/span/span[2]/text()')
        else:
            l.add_value('normal_price', '')

        # if self.isExist('#price, soup):
        #     l.add_xpath('now_price', '//p[@id="price"]')
        # else:
        #     l.add_value('now_price', '')

        # if self.isExist('#popbox > div > div > h3 > a', soup):
    #         l.add_xpath('mon_sales', '//p[@id="price"]')
        # else:
        #     l.add_value('mon_sales', '')

        if self.isExist('#comment-count > a', soup):
            l.add_xpath('total_views', '//div[@id="comment-count"]/a/text()')
        else:
            l.add_value('total_views', '')

        # if self.isExist('#popbox > div > div > h3 > a', soup):
        #     l.add_xpath('stock', '//p[@id="price"]')
        # else:
        #     l.add_value('stock', '')

        if self.isExist('#parameter-brand > li > a', soup):
            l.add_xpath('brand', '//ul[@id="parameter-brand"]/li/a/text()')
        else:
            l.add_value('brand', '')

        if self.isExist('.p-parameter > ul', soup):
            details = soup.select('.p-parameter > ul[3] > li')
            for i in range(len(details)):
                l.add_value('item{}'.format(i), details[i].string)
        else:
            for i in range(6):
                l.add_value('item{}'.format(i), '')

        return l.load_item

