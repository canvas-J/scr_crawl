# -*- coding: utf-8 -*-
import scrapy, re
from zhihu.items import ZhihuItem


class ViewSpider(scrapy.Spider):
    name = 'article'
    # custom_settings = {
    #     # specifies exported fields and order
    #     'FEED_EXPORT_FIELDS': ["rate_id", "pinglun", "shijian1", "score", "guige", "guige1", "yonghuming"],
    #     }
    start_urls = ['https://www.zhihu.com/topic/19836247/hot']

    def parse(self, response):
        if response.status==200:
            arts = response.xpath('//div[@id="TopicMain"]/div/div/div/div[@class=""]/*')
            for message in arts:
                link = 'https://www.zhihu.com' + str(message.xpath('.//h2[@class="ContentItem-title"]/div/a/@href').extract_first())
                if len(link) > 30:
                    yield scrapy.Request(link, callback=self.parse_item)
        elif response.status==202:
            yield scrapy.Request(response.url, callback=self.parse, dont_filter=True)

    def parse_item(self, response):
        if response.status==200:
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            name = response.xpath('//h1[@class="QuestionHeader-title"]/text()')
            answers = response.xpath('//div[@id="QuestionAnswers-answers"]/div/div/div/div[@class=""]/*')
            for message in answers:
                item = ZhihuItem()
                item["que_name"] = name.extract_first()
                item["link"] = response.url
                item["user_id"] = message.xpath('.//div[@class="Popover"]/div/a/text()').extract_first()
                item["user_link"] = 'https:' + str(message.xpath('.//div[@class="Popover"]/div/a/@href').extract_first())
                item["praise"] = message.xpath('.//div[@class="AnswerItem-extraInfo"]/span/button/text()').extract_first()
                item["comments"] = message.xpath('.//div[@class="ContentItem-actions"]/button[1]/text()').extract_first()
                article = message.xpath('string(.//div[@class="RichContent-inner"]/span)').extract_first()
                pattern = re.compile(r'<.*?>', re.S)
                clean_article = pattern.sub('', article) 
                item["article"] = clean_article
                item["pub_time"] = message.xpath('.//div[@class="ContentItem-time"]/a/span/@data-tooltip').extract_first()
                item["edit_time"] = message.xpath('.//div[@class="ContentItem-time"]/a/span/text()').extract_first()
                yield item
        elif response.status==202:
            yield scrapy.Request(response.url, callback=self.parse_item, dont_filter=True)
