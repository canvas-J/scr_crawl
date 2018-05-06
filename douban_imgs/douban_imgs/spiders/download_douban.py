# coding=utf-8
from scrapy.spiders import Spider
import re
import scrapy
from scrapy import Request
from douban_imgs.items import DoubanImgsItem
# 导入CrawlSpider类和Rule
from scrapy.spiders import CrawlSpider, Rule
# 导入链接规则匹配类，用来提取符合规则的连接
from scrapy.linkextractors import LinkExtractor
 
class download_douban(Spider):
    name = 'download_douban'
    allowed_domains = ['douban.com']
    # start_urls = ['http://www.douban.com/photos/album/1638835355/']

    default_headers = {
    'accept': 'image/webp,image/*,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, sdch, br',
    'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'cookie': 'bid=yQdC/AzTaCw',
    'referer': 'https://www.douban.com/photos/photo/2370443040/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }
 

    # pagelink = LinkExtractor(allow=("http://www.douban.com/photos/album/1638835355/"))
    # rules = [Rule(pagelink, 'parse', follow=True)]

    def start_requests(self):
        urls = ['http://www.douban.com/photos/album/1638835355/?start=0']
        for url in urls:
            yield scrapy.Request(url, headers=self.default_headers)

    def parse(self, response):
        list_imgs = response.xpath('//div[@class="photolst clearfix"]//img/@src').extract()
        if list_imgs:
            item = DoubanImgsItem()
            item['image_urls'] = list_imgs
            yield item

        next_page = response.xpath('//span[@class="thispage"]/following-sibling::a[1]/@href').extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page, headers=self.default_headers, callback=self.parse)