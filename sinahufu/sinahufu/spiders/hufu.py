# -*- coding: utf-8 -*-
from scrapy import Spider,Request


class HufuSpider(Spider):
    name = 'hufu'
    start_urls = ['https://d.weibo.com/1087030002_2976_2014_5#']

    def parse(self, response):
        selector = response.xpath('//li[@class="follow_item S_line2"]/dl/dd/div/a/@href').extract()
        for url in selector:
            yield Request(url=url, callback=self.parse_item)

    def parse_item(self, response, next_url):
        items = response.xpath('//div[@class="WB_cardwrap WB_feed_type S_bg2 WB_feed_vipcover WB_feed_like "]/div/div/div[@class="WB_text W_f14"]/[@text]').extract()
        # item2 = response.xpath('//div[contains(@class, "item J_MouserOnverReq")]/div/div/a/@href').extract()
        # item3 = response.xpath('//div[contains(@class, "item J_MouserOnverReq")]/div/div/a/@href').extract()
        # item4 = response.xpath('//div[contains(@class, "item J_MouserOnverReq")]/div/div/a/@href').extract()
        # item5 = response.xpath('//div[contains(@class, "item J_MouserOnverReq")]/div/div/a/@href').extract()
        # with open('hufu.txt', 'wt') as f:
        #     for i in range(1, 6):
        #         f.write(item[i])
        with open('hufu.txt', 'wt') as f:
            for item in items:
                f.write(item)
            