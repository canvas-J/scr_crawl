# -*- encoding: utf-8 -*-
import scrapy
import random

class ProcessHeaderMidware():
    
    def process_request(self, request, spider):
        useragent = random.choice(scrapy.crawler.Settings.get('USER_AGENT_LIST'))
        spider.logger.info(msg='now entring download midware')
        if useragent:
            request.headers['User-Agent'] = useragent
            # Add desired logging message here.
            spider.logger.info('User-Agent is : {} {}'.format(request.headers.get('User-Agent'), request))
        pass