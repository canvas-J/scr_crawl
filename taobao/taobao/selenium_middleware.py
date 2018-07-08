from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException
import time, random

class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        if request.url == 'https://www.taobao.com/':
            try:
                spider.browser.get(request.url)
                spider.browser.get(request.url)
                spider.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(random.randint(1, 2))
                return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source,
                                encoding="utf-8", request=request, next_url=self.next_url)
            except TimeoutException:
                print('超时')
                spider.browser.execute_script('window.stop()')
        else:
            try:
                spider.browser.get(request.url)
                time.sleep(1)
                spider.browser.execute_script('window.scrollTo(0, document.body.scrollHeight*2/5)')
                time.sleep(2)
                return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source,
                                encoding="utf-8", request=request, next_url=self.next_url)
            except TimeoutException:
                print('超时')
                spider.browser.execute_script('window.stop()')