# -*- coding: utf-8 -*-
import requests

class MyproxiesMidware(object):

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(crawler.settings)

    # def __init__(self, crawler):
    #     self.IPpool = crawler.settings.get('IPPOOL')
    
    def process_request(self, request, spider):
        proxy = requests.get("http://192.168.1.153/get/").text
        print("current ip:" + proxy)
        request.meta["proxy"] = "http://" + proxy