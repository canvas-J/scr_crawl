from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException
import time

class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        if request.url == 'http://www.jd.com/':
            try:
                spider.browser.get(request.url)
                # 找到搜索框，清除，输入关键字
                search = spider.browser.find_element_by_xpath('//input[@clstag="h|keycount|head|search_a"]')
                search.clear()
                search.send_keys('手机')

                # submit
                # sub_btn = spider.browser.find_element_by_xpath('//button[@class="btn-search tb-bg"]')  
                # sub_btn.click()  
                time.sleep(0.5)
                # 点击搜索
                xlpx = spider.browser.find_element_by_xpath('//button[@clstag="h|keycount|head|search_c"]')
                xlpx.click()
                time.sleep(1)

                # url = 'https://search.jd.com/Search?keyword=%E7%94%B7%E5%A3%AB%E6%B4%81%E9%9D%A2&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%94%B7%E5%A3%AB%E6%B4%81%E9%9D%A2&page=1&s=1&click=0'
                # spider.browser.get(url)
                # time.sleep(5)
                # commentrank = spider.browser.find_element_by_xpath('//a[@ onclick="SEARCH.sort('4')"]')
                # commentrank.click()  
                # time.sleep(2)
                # 获取总页数
                span_num = spider.browser.find_element_by_xpath('//span[@class="fp-text"]')
                page_num = span_num.text.split('/')
                print("已获取第{}页，总共{}页".format(page_num[0], page_num[-1]))
                spider.browser.execute_script('window.scrollTo(0, document.body.scrollHeight-300)')
                time.sleep(2)              

                return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source,
                                encoding="utf-8", request=request)
            except TimeoutException as e:
                print('超时')
                spider.browser.execute_script('window.stop()')
        else:
            try:
                spider.browser.get(request.url)
                time.sleep(1)
                spider.browser.execute_script('window.scrollTo(0, document.body.scrollHeight-300)')
                time.sleep(2)

                return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source,
                                encoding="utf-8", request=request)

            except TimeoutException as e:
                print('超时')
                spider.browser.execute_script('window.stop()')
            time.sleep(2)