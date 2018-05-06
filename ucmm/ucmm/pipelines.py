# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
# import os


class JiandanPipeline(object):
    def process_item(self, item, spider):
        return item

class MeizituDownloadPipeline(ImagesPipeline):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',\
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',\
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'
    }
 
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            self.headers['referer'] = image_url
            yield Request(image_url, headers=self.headers)
 
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item



    # 重载该方法后名字依然不友好，选择重载item_completed调用系统函数重命名
    # def file_path(self,request, response=None, info=None):
        # item = request.meta['item']
        # image_guid = item['fname']+'.jpg'
        #image_guid = request.url.split('/')[-1]
        # filename = u'full/{0[mote_id]}/{1}'.format(item,image_guid)
        # filename = 'full/{0}'.format(image_guid)
        # image_guid = request.url.split('/')[-1]
        # return 'full/%s' % (image_guid)