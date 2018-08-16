# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from scrapy.loader import ItemLoader
from atobodetail.items import AtobodetailItem

class CdetailSpider(scrapy.Spider):

    name = 'cdetail'
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["url", "category", "hangye", "quxian", "ximu", "mingcheng", "zhuangtai", "zhucehao", 
        "farendaibiao", "zhuceziben", "qiyeleixing", "degnjijiguan", "chegnliriqi", "yingyeqixian", "jingyingfanwei", 
        "zhucedizhi", "gaoguan1", "zhiwei1", "gaoguan2", "zhiwei2", "gaoguan3", "zhiwei3", "gaoguan4", "zhiwei4", 
        "gudong1", "renjiao1", "shijiao1", "chigubili1", "gudong2", "renjiao2", "shijiao2", "chigubili2", "gudong3", 
        "renjiao3", "shijiao3", "chigubili3", "duiwaitouzi", "wangdian1", "lianxiren1", "lianxidianhua1", "shouji1", 
        "zhuyingchanpin1", "wangdian2", "lianxiren2", "lianxidianhua2", "shouji2", "zhuyingchanpin2"],
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.all_links = pd.DataFrame(pd.read_csv('sh_links_02.csv',encoding='gb18030'))

    def start_requests(self):
        urls = list(self.all_links.ix[:, "bu_links"])
        for num, url in enumerate(urls):
            if "http" not in str(url):
                continue
            category = str(self.all_links.iloc[num, 4])
            hangye = str(self.all_links.iloc[num, 6])
            quxian = str(self.all_links.iloc[num, 7])
            ximu = str(self.all_links.iloc[num, 8])
            yield scrapy.Request(url=url, callback=self.parse_item, meta={'category': category, 'hangye': hangye, 'quxian': quxian, 'ximu': ximu})

    # def parse_company(self, response):
    #     l = ItemLoader(item=AtobodetailItem(), response=response)
    #     # 使用add_xpath方法，传递Item类的字段名称和对应的xpath解析语法
    #     l.add_xpath('shop_name', '//div[@class="product_name"]')
    #     l.add_xpath('goods_name', '//div[@class="product_title"]')
    #     l.add_xpath('normal_price', '//p[@id="price"]')
    #     l.add_xpath('now_price', '//p[@id="price"]')
    #     l.add_xpath('mon_sales', '//p[@id="price"]')
    #     l.add_xpath('total_views', '//p[@id="price"]')
    #     l.add_xpath('stock', '//p[@id="price"]')
    #     l.add_xpath('brand', '//p[@id="price"]')
    #     l.add_xpath('delivery_port', 'p#stock]')
    #     l.add_xpath('platform', 'today')
    #     return l.load_item

    def parse_item(self, response):
        if response.status==200:
            m = ItemLoader(item=AtobodetailItem(), response=response)
            m.add_value('url', response.url)
            m.add_value('category', response.meta['category'])
            m.add_value('hangye', response.meta['hangye'])
            m.add_value('quxian', response.meta['quxian'])
            m.add_value('ximu', response.meta['ximu'])
            m.add_xpath('mingcheng', '//*[@id="f1"]/ul[2]/li[1]/div/table/tbody/tr[1]/td[2]/text()')
            m.add_xpath('zhuangtai', '//*[@id="f1"]/ul[2]/li[1]/div/table/tbody/tr[2]/td[2]/text()')
            m.add_xpath('zhucehao', '//*[@id="f1"]/ul[2]/li[1]/div/table/tbody/tr[2]/td[4]/text()')
            m.add_xpath('farendaibiao', '//*[@id="f1"]/ul[2]/li[1]/div/table/tbody/tr[3]/td[2]/a/text()')
            m.add_xpath('zhuceziben', '//*[@id="f1"]/ul[2]/li[1]/div/table/tbody/tr[3]/td[4]/text()')
            m.add_xpath('qiyeleixing', '//*[@id="f1"]/ul[2]/li[1]/div/table/tbody/tr[4]/td[2]/text()')
            m.add_xpath('dengjijiguan', '//*[@id="f1"]/ul[2]/li[1]/div/table/tbody/tr[4]/td[4]/text()')
            m.add_xpath('chengliriqi', '//*[@id="f1"]/ul[2]/li[1]/div/table/tbody/tr[5]/td[2]/text()')
            m.add_xpath('yingyeqixian', '//*[@id="f1"]/ul[2]/li[1]/div/table/tbody/tr[5]/td[4]/text()')
            m.add_xpath('jingyingfanwei', '//*[@id="f1"]/ul[2]/li[1]/div/table/tbody/tr[6]/td[2]/text()')
            m.add_xpath('zhucedizhi', '//*[@id="f1"]/ul[2]/li[1]/div/table/tbody/tr[7]/td[2]/text()')
            m.add_xpath('gaoguan1', '//*[@id="f2"]/ul[2]/li[1]/div/ul/li[1]/div/ul/li[2]/a/text()')
            m.add_xpath('zhiwei1', '//*[@id="f2"]/ul[2]/li[1]/div/ul/li[1]/div/ul/li[3]')
            m.add_xpath('gaoguan2', '//*[@id="f2"]/ul[2]/li[1]/div/ul/li[2]/div/ul/li[2]/a/text()')
            m.add_xpath('zhiwei2', '//*[@id="f2"]/ul[2]/li[1]/div/ul/li[2]/div/ul/li[3]')
            m.add_xpath('gaoguan3', '//*[@id="f2"]/ul[2]/li[1]/div/ul/li[3]/div/ul/li[2]/a/text()')
            m.add_xpath('zhiwei3', '//*[@id="f2"]/ul[2]/li[1]/div/ul/li[3]/div/ul/li[3]')
            m.add_xpath('gaoguan4', '//*[@id="f2"]/ul[2]/li[1]/div/ul/li[4]/div/ul/li[2]/a/text()')
            m.add_xpath('zhiwei4', '//*[@id="f2"]/ul[2]/li[1]/div/ul/li[4]/div/ul/li[3]')
            m.add_xpath('gudong1', '//*[@id="f3"]/ul[2]/li[1]/div/table/tbody/tr[2]/td[1]/a/text()')
            m.add_xpath('renjiao1', '//*[@id="f3"]/ul[2]/li[1]/div/table/tbody/tr[2]/td[2]/text()')
            m.add_xpath('shijiao1', '//*[@id="f3"]/ul[2]/li[1]/div/table/tbody/tr[2]/td[3]/text()')
            m.add_xpath('chigubili1', '//*[@id="f3"]/ul[2]/li[1]/div/table/tbody/tr[2]/td[4]/text()')
            m.add_xpath('gudong2', '//*[@id="f3"]/ul[2]/li[1]/div/table/tbody/tr[3]/td[1]/a/text()')
            m.add_xpath('renjiao2', '//*[@id="f3"]/ul[2]/li[1]/div/table/tbody/tr[3]/td[2]/text()')
            m.add_xpath('shijiao2', '//*[@id="f3"]/ul[2]/li[1]/div/table/tbody/tr[3]/td[3]/text()')
            m.add_xpath('chigubili2', '//*[@id="f3"]/ul[2]/li[1]/div/table/tbody/tr[3]/td[4]/text()')
            m.add_xpath('gudong3', '//*[@id="f3"]/ul[2]/li[1]/div/table/tbody/tr[4]/td[1]/a/text()')
            m.add_xpath('renjiao3', '//*[@id="f3"]/ul[2]/li[1]/div/table/tbody/tr[4]/td[2]/text()')
            m.add_xpath('shijiao3', '//*[@id="f3"]/ul[2]/li[1]/div/table/tbody/tr[4]/td[3]/text()')
            m.add_xpath('chigubili3', '//*[@id="f3"]/ul[2]/li[1]/div/table/tbody/tr[4]/td[4]/text()')
            m.add_xpath('duiwaitouzi', '//*[@id="f4"]/ul[2]/li[1]/text()')
            m.add_xpath('wangdian1', '//*[@id="f5"]/ul[2]/li[1]/div/ul/li[1]/div/ul/li[1]/a/text()')
            m.add_xpath('lianxiren1', '//*[@id="f5"]/ul[2]/li[1]/div/ul/li[1]/div/ul/li[2]/text()')
            m.add_xpath('lianxidianhua1', '//*[@id="f5"]/ul[2]/li[1]/div/ul/li[1]/div/ul/li[4]/span/text()')
            m.add_xpath('shouji1', '//*[@id="f5"]/ul[2]/li[1]/div/ul/li[1]/div/ul/li[5]/span/text()')
            m.add_xpath('zhuyingchanpin1', '//*[@id="f5"]/ul[2]/li[1]/div/ul/li[1]/div/ul/li[6]/text()')
            m.add_xpath('wangdian2', '//*[@id="f5"]/ul[2]/li[1]/div/ul/li[2]/div/ul/li[1]/a/text()')
            m.add_xpath('lianxiren2', '//*[@id="f5"]/ul[2]/li[1]/div/ul/li[2]/div/ul/li[2]/text()')
            m.add_xpath('lianxidianhua2', '//*[@id="f5"]/ul[2]/li[1]/div/ul/li[2]/div/ul/li[4]/span/text()')
            m.add_xpath('shouji2', '//*[@id="f5"]/ul[2]/li[1]/div/ul/li[2]/div/ul/li[5]/span/text()')
            m.add_xpath('zhuyingchanpin2', '//*[@id="f5"]/ul[2]/li[1]/div/ul/li[2]/div/ul/li[6]/text()')
            yield m.load_item()
        elif response.status==202:
            category = response.meta['category']
            hangye = response.meta['hangye']
            quxian = response.meta['quxian']
            ximu = response.meta['ximu']
            yield scrapy.Request(response.url, callback=self.parse_item, dont_filter=True, meta={'category': category, 'hangye': hangye, 'quxian': quxian, 'ximu': ximu})
