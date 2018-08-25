# -*- coding: utf-8 -*-

# Scrapy settings for atobodetail project
BOT_NAME = 'atobodetail'
SPIDER_MODULES = ['atobodetail.spiders']
NEWSPIDER_MODULE = 'atobodetail.spiders'
JOBDIR='detail_dir'

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 9
# DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS_PER_IP = 1
COOKIES_ENABLED = False
DEFAULT_REQUEST_HEADERS = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

DOWNLOADER_MIDDLEWARES = {
    'atobodetail.ProxyMidware.MyproxiesMidware': 500,
    'atobodetail.multi_selenium.SeleniumMiddleware': 350,
    'atobodetail.UseragentMidware.RandomUseragentMidware': 520, 
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
    }

# ITEM_PIPELINES = {
#    'atobodetail.pipelines.AtobodetailPipeline': 200,
# }


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
#SPIDER_MIDDLEWARES = {
#    'atobodetail.middlewares.AtobodetailSpiderMiddleware': 543,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
