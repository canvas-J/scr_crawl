# -*- coding: utf-8 -*-
import scrapy, json, re
from review.items import ReviewItem
import pandas as pd


class ViewSpider(scrapy.Spider):
    name = 'jd_review'
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["rate_id", "pinglun", "shijian1", "score", "guige", "guige1", "yonghuming"],
        }

    def start_requests(self):
        df = pd.read_excel('评论链接.xlsx', encoding='gb18030')
        for i in range(100):
            for row in range(len(df)):
                yield scrapy.Request(url="https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv7796&productId={}&score=0&sortType=6&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1".format(df.ix[row,'productid'], i+1),
                        callback=self.parse, meta={'rate_id': df.ix[row,'productid']})

    def parse(self, response):
        if response.status==200:
            comment_json = response.xpath('/html/body/text()').extract_first() # 获取到jsonp
            pattern = re.compile(r'[(](.*)[)]', re.S)
            json_data = re.findall(pattern, comment_json)[0] # 将jsonp或jQuery解析为json
            hjson = json.loads(json_data)
            for message in hjson["comments"]:
                item = ReviewItem()
                item["rate_id"] = response.meta['rate_id']
                item["guige"] = message["productColor"]
                item["guige1"] = message["productSize"]
                item["pinglun"] = message["content"]
                item["shijian1"] = message["creationTime"]
                item["score"] = message["score"]
                item["yonghuming"] = message["nickname"]
                yield item   
        elif response.status==202:
            rate_id = response.meta['rate_id']
            yield scrapy.Request(response.url, callback=self.parse, dont_filter=True, meta={'rate_id': rate_id})
