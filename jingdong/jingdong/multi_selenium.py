from selenium import webdriver
from scrapy.http import HtmlResponse
from fake_useragent import UserAgent
from scrapy.exceptions import IgnoreRequest
from queue import Queue
from scrapy.utils.project import get_project_settings
import time, random

class SeleniumMiddleware(object):
    def __init__(self):
        # Initialize browser
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.add_argument('disable-infobars')
        options.add_argument('useragent="{}"'.format(UserAgent().random))
        self.browser = webdriver.Chrome(chrome_options=options)

        # get project settings
        settings=get_project_settings()
        concurrent_requests=settings.get('CONCURRENT_REQUESTS')

        # Initialize tabs
        while len(self.browser.window_handles) < concurrent_requests:
            self.browser.execute_script('''window.open("","_blank");''')

        # Initialize window handles queue
        self.handle_queue=Queue(maxsize=concurrent_requests)
        for handle in self.browser.window_handles:
            self.handle_queue.put(handle)

        # Initialize requests dict
        self.requests={}

    def process_request(self, request, spider):
        result=self.requests.get(request.url)
        if result is None:
            # get a free window_handle from queue
            if self.handle_queue.empty():
                return HtmlResponse(url=request.url,request=request, encoding='utf-8', status=202)
            handle = self.handle_queue.get()

            # open url by js
            self.browser.switch_to.window(handle)
            js = r"location.href='%s';" % request.url
            self.browser.execute_script(js)

            # wait for 1s to avoid some bug ("document.readyState" will return a "complete" at the first)
            time.sleep(0.5)

            # mark url
            self.requests[request.url]={'status':'waiting','handle':handle}

            return HtmlResponse(url=request.url,request=request, encoding='utf-8', status=202)

        elif result['status']=='waiting':

            # switch to the tab to check page status using javascript
            handle = result['handle']
            self.browser.switch_to.window(handle)
            document_status=self.browser.execute_script("return document.readyState;")

            if document_status=='complete':
                if 'search.jd.com' in request.url:
                        self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight/2)')
                        time.sleep(0.5)
                        self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight*7/10)')
                        time.sleep(1.2)
                        self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                        time.sleep(0.8)
                elif 'item.jd.com' in request.url:
                        self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight*2/5)')
                        time.sleep(0.5)
                self.requests[request.url]['status'] = 'done'
                self.handle_queue.put(handle)
                return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                                    status=200)
            else:
                return HtmlResponse(url=request.url, request=request, encoding='utf-8', status=202)

        elif result['status']=="done":
            # Filter repeat URL
            raise IgnoreRequest

    def __del__(self):
        self.browser.quit()
