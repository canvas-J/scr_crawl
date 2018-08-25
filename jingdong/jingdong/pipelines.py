# -*- coding: utf-8 -*-
# import pymongo
# from scrapy.conf import settings

# from scrapy.exporters import JsonItemExporter # 以json格式输出
# from scrapy.exporters import JsonLinesItemExporter # 以jl格式输出
from scrapy.exporters import CsvItemExporter # 以csv格式输出


class OutputPipeline(object):

    def open_spider(self, spider):
        self.file = open('review-8-15.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='gb18030')
        self.exporter.start_exporting()

    def close_spier(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

'''
class MongoPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT']) # 建条高速路
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]  # 小货车--获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']]  # 小货车--获得collection的句柄

    def process_item(self, item, spider):
        postItem = dict(item)       # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        return item                 # 在控制台输出item数据
'''