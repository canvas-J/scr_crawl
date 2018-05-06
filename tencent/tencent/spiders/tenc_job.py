# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem
# 导入CrawlSpider类和Rule
from scrapy.spiders import CrawlSpider, Rule
# 导入链接规则匹配类，用来提取符合规则的连接
from scrapy.linkextractors import LinkExtractor


class TencJobSpider(scrapy.Spider):
    name = 'tenc_job'
    allowed_domains = ['tencent.com']
    start_urls = ["http://hr.tencent.com/position.php?&start=00#a"]

    # pagelink = LinkExtractor(allow=("position.php?&start=\d+"))

    # rules = [Rule(pagelink, 'parse', follow=True)]

    def parse(self, response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            item = TencentItem()
            item['position_name'] = each.xpath('./td[1]/a/text()').extract_first()
            item['position_link'] = each.xpath('./td[1]/a/@href').extract_first()
            item['position_type'] = each.xpath('./td[2]/text()').extract_first()
            item['position_num'] = each.xpath('./td[3]/text()').extract_first()
            item['work_location'] = each.xpath('./td[4]/text()').extract_first()
            item['publish_time'] = each.xpath('./td[5]/text()').extract_first()

            yield item

        next_page = response.xpath('//a[@class="active"]/following-sibling::a[1]/@href').extract_first()
        if next_page is not None:
            next_page = "http://hr.tencent.com/" + next_page
            yield scrapy.Request(next_page, callback=self.parse)