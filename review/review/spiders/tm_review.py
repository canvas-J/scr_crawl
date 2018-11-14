# -*- coding: utf-8 -*-
import scrapy, json, re
from review.items import ReviewItem
import pandas as pd


class ViewSpider(scrapy.Spider):
    name = 'tm_review'
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["rate_id", "pinglun", "shijian1", "zhuiping", "shijian2", "guige", "yonghuming"],
        }

    def start_requests(self):
        '''
        属性值、特性相同的商品就可以称为一个SPU,Standard Product Unit （标准化产品单元）
        '''

        df = pd.read_excel('评论链接.xlsx', encoding='gb18030')
        for i in range(100):
            for row in range(len(df)):
                yield scrapy.Request(url="https://rate.tmall.com/list_detail_rate.htm?itemId={}&sellerId={}&order=1&currentPage={}&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098".format(df.ix[row,'itemid'], df.ix[row,'sellerid'], i+1),
                        callback=self.parse, meta={'rate_id': df.ix[row,'itemid']})

    def parse(self, response):
        if response.status==200:
            comment_json = response.xpath('/html/body/text()').extract_first() # 获取到jsonp
            pattern = re.compile(r'[(](.*)[)]', re.S)
            json_data = re.findall(pattern, comment_json)[0] # 将jsonp解析为json
            hjson = json.loads(json_data)
            for message in hjson["rateDetail"]["rateList"]:
                item = ReviewItem()
                item["rate_id"] = response.meta['rate_id']
                item["guige"] = message["auctionSku"]
                item["pinglun"] = message["rateContent"]
                item["shijian1"] = message["rateDate"]
                if message["appendComment"] != None:
                    item["zhuiping"] = message["appendComment"]["content"]
                    item["shijian2"] = message["appendComment"]["commentTime"]
                else:
                    item["zhuiping"] = ""
                    item["shijian2"] = ""  
                item["yonghuming"] = message["displayUserNick"]
                yield item   
        elif response.status==202:
            rate_id = response.meta['rate_id']
            yield scrapy.Request(response.url, callback=self.parse, dont_filter=True, meta={'rate_id': rate_id})
