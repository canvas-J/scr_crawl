# -*- coding: utf-8 -*-


BOT_NAME = 'review'
SPIDER_MODULES = ['review.spiders']
NEWSPIDER_MODULE = 'review.spiders'
# JOBDIR='review_dir'

ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False
CONCURRENT_REQUESTS = 12
# DOWNLOAD_DELAY = 1
# RANDOMIZE_DOWNLOAD_DELAY = True
# CONCURRENT_REQUESTS_PER_IP = 1

DEFAULT_REQUEST_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'Accept-Encoding': 'gzip'}

DOWNLOADER_MIDDLEWARES = {
    # 'review.ProxyMidware.MyproxiesMidware': 100,
    'review.multi_selenium.SeleniumMiddleware': 542,
    'review.UseragentMidware.RandomUseragentMidware': 110, 
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
    }

# ITEM_PIPELINES = {
#    'review.pipelines.OutputPipeline': 200,
# }

# MONGO_HOST = "127.0.0.1"
# MONGO_PORT = 27017
# MONGO_DB = "Spider"       # 库名 
# MONGO_COLL = "heartsong"  # collection
# MONGO_USER = "zhangsan"
# MONGO_PSW = "123456"

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

#SPIDER_MIDDLEWARES = {
#    'review.middlewares.ReviewSpiderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
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
