# -*- coding: utf-8 -*-
import scrapy, time
import pandas as pd
from scrapy_redis.spiders import RedisSpider
from atobourl.items import AtobourlItem


class ClinksSpider(RedisSpider):
    name = 'clinks'
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["quxian", "hangye", "ximu", "category", "c_name", "colinks", "bulinks", "c_product", "c_address"],
        }
    redis_key = "clinks:start_urls" # https://www.atobo.com.cn/Companys

    def parse(self, response):
        all_class = pd.DataFrame(pd.read_excel('class.xlsx'))
        quxian = list(all_class.ix[:,'区县类别'])
        ximu = list(all_class.ix[:,'细目类别'])
        for qu in quxian:
            for xi in ximu:
                if "q" in str(qu) and "c" in str(xi):
                    url = '{}s-p2-s871-{}-{}/'.format(response.url, qu, xi)
                    yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        for company in response.xpath('//li[@class="product_box"]'):
            item = AtobourlItem()
            try:
                message = response.xpath('//div[@class="filterMode"]/h2/span/a[4]/text()').extract_first().split('：')[-1]
                item['quxian'] = response.xpath('//div[@class="filterMode"]/h2/span/a[3]/text()').extract_first().split('：')[-1]
            except:
                message = response.xpath('//div[@class="filterMode"]/h2/span/a[3]/text()').extract_first().split('：')[-1]
                item['quxian'] = ""
            item['hangye'] = message.split('>')[0].strip()
            try:
                item['ximu'] = message.split('>')[1].strip()
            except:
                item['ximu'] = ""
            item['category'] = response.xpath('//div[@class="filterMode"]/h2/strong/text()').extract_first()
            item['co_links'] = "https:" + company.xpath('.//a[@class="CompanyName"]/@href').extract_first()
            g_url = company.xpath('.//li[@class="pp_name"]/a[3]/@href').extract_first()
            if g_url != None:
                item['bu_links'] = "https:" + str(g_url)
            elif company.xpath('.//li[@class="pp_name"]/a[2]/@href').extract_first() != None:
                item['bu_links'] = "https:" + str(company.xpath('.//li[@class="pp_name"]/a[2]/@href').extract_first())
            else:
                item['bu_links'] = ""
            item['c_name'] = company.xpath('.//a[@class="CompanyName"]/text()').extract_first()
            item['c_product'] = company.xpath('string(.//li[@class="pp_product"])').extract()
            item['c_address'] = company.xpath('string(.//li[@class="pp_address"])').extract()
            yield item

        if '-y' not in response.url:
            total_page = response.xpath('//li[@class="spagelist"]/strong[2]/text()').extract_first()
            print(total_page)
            if int(total_page) > 50:
                total_page = 50
            elif int(total_page) < 1:
                pass
            else:
                for page in range(2, int(total_page)+1):
                    url = response.url + "-y{}/".format(page)
                    yield scrapy.Request(url=url, callback=self.parse_item)
