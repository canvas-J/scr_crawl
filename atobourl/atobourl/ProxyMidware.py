# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
import random, requests

'''
class ProxyTool(object):

    def __init__(self):
        pass

    def get_proxy(self):
        return requests.get("http://127.0.0.1:5010/get/").text

    def delete_proxy(self, proxy):
        requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

    def ip_test(self, proxy, url_for_test, headers, set_timeout=2):
        try:
            r = requests.get(url_for_test, headers=headers, proxies={'http': "http://{}".format(proxy)}, timeout=2)
            if r.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def test_proxy(self):
        ip_list = []
        headers = {'User-Agent': UserAgent().random,
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            'Accept-Encoding': 'gzip'
            }
        for i in range(30):
            proxy = self.get_proxy()
            # if self.ip_test(proxy, 'https://www.taobao.com/', headers):
            if self.ip_test(proxy, 'https://detail.tmall.com/', headers):
                print(proxy)
                ip_list.append('http://'+proxy)
            else:
                self.delete_proxy(proxy)
                print('代理不可用')
        print("30个ip有{}个可用..".format(len(ip_list)))
        return ip_list
'''

class MyproxiesMidware(object):

    def __init__(self, crawler):
        # self.IPpool = ProxyTool().test_proxy
        self.IPpool = crawler.settings.get('IPPOOL')
    
    def process_request(self, request, spider):
        current_ip = random.choice(self.IPpool)
        print("current ip:"+current_ip["ip"])
        request.meta["proxy"] = "http://" + current_ip["ip"]