# -*- coding: utf-8 -*-
import scrapy, time
from atobourl.items import AtobourlItem


class ClinksSpider(scrapy.Spider):
    name = 'clinks'
    allowed_domains = ['www.atobo.com.cn']
    start_urls = ['https://www.atobo.com.cn/Companys/']

    def parse(self, response):
        num = 0
        for each_url in response.xpath('//li[contains(@id, "filter")]'):
            num += 1
            if num > 8:
                links = 'https://www.atobo.com.cn' + each_url.xpath('.//a/@href').extract_first()
                yield scrapy.Request(url=links, callback=self.parse_item)

    def parse_item(self, response):
        for company in response.xpath('//li[@class="product_box"]'):
            item = AtobourlItem()
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
                for page in range(2, int(total_page)+1):
                    url = response.url + "-y{}/".format(page)
                    yield scrapy.Request(url=url, callback=self.parse_item)