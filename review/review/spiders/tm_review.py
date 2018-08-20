# -*- coding: utf-8 -*-
import scrapy, json, re
from review.items import ReviewItem


class ViewSpider(scrapy.Spider):
    name = 'tm_review'
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["rate_id", "pinglun", "shijian1", "zhuiping", "shijian2", "guige", "yonghuming"],
        }

    def start_requests(self):
        links = []
        for i in range(100):
            links.append("https://rate.tmall.com/list_detail_rate.htm?itemId=544777674225&spuId=722377432&sellerId=2987441916&order=1&currentPage={}&append=0&content=1&tagId=&posi=&picture=&ua=098".format(i+1))
            links.append("https://rate.tmall.com/list_detail_rate.htm?itemId=544529437073&spuId=721054050&sellerId=2509849149&order=1&currentPage={}&append=0&content=1&tagId=&posi=&picture=&ua=098".format(i+1))
            links.append("https://rate.tmall.com/list_detail_rate.htm?itemId=531869578250&spuId=573117493&sellerId=748612647&order=1&currentPage={}&append=0&content=1&tagId=&posi=&picture=&ua=098".format(i+1))
            links.append("https://rate.tmall.com/list_detail_rate.htm?itemId=549983235705&spuId=693976831&sellerId=2963458513&order=1&currentPage={}&append=0&content=1&tagId=&posi=&picture=&ua=098".format(i+1))
            links.append("https://rate.tmall.com/list_detail_rate.htm?itemId=544828890290&spuId=721092887&sellerId=3014868997&order=1&currentPage={}&append=0&content=1&tagId=&posi=&picture=&ua=098".format(i+1))
        for url in links:
            rate_id = url[51:63]
            yield scrapy.Request(url=url, callback=self.parse, meta={'rate_id': rate_id})

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
