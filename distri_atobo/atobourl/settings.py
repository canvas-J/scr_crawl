# -*- coding: utf-8 -*-

# Scrapy settings for atobourl project
BOT_NAME = 'atobourl'
SPIDER_MODULES = ['atobourl.spiders']
NEWSPIDER_MODULE = 'atobourl.spiders'
JOBDIR='company_messages'

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 6
DOWNLOAD_DELAY = 10
RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False


# 使用scrapy-redis里的去重组件，不使用scrapy默认的去重方式
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy-redis里的调度器组件，不使用默认的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 允许暂停，redis请求记录不丢失
SCHEDULER_PERSIST = True
# 默认的scrapy-redis请求队列形式（按优先级）
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 队列形式，请求先进先出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 栈形式，请求先进后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

'''
IPPOOL = [
    {"ip":"171.10.31.73:8080"},
    {"ip":"221.7.255.167:8080"},
    {"ip":"101.96.11.5:80"},
    {"ip":"219.141.153.39:80"},
    {"ip":"117.127.0.203:8080"},
    {"ip":"101.96.10.5:80"},
    {"ip":"120.24.49.226:8080"},
    {"ip":"117.127.0.205:8080"},
    {"ip":"120.24.49.226:8080"},
    {"ip":"120.24.49.226:8080"},
    {"ip":"117.127.0.195:8080"},
    {"ip":"117.127.0.201:8080"},
    {"ip":"202.100.83.139:80"},
    {"ip":"59.44.16.6:8080"}
]
'''

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
        # 'atobourl.ProxyMidware.MyproxiesMidware': 541,
        # 'atobourl.multi_selenium.SeleniumMiddleware': 542,
        'atobourl.UseragentMidware.RandomUseragentMidware': 543, 
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
        }

# ITEM_PIPELINES = {
#     'scrapy_redis.pipelines.RedisPipeline': 200
# }


# 优先
REDIS_URL = 'redis://@192.168.1.179:6379'
# # 第一种指定数据库方法
# REDIS_URL = 'redis://@192.168.1.179:6379/1'
# # 第二种指定数据库方法
# REDIS_PARAMS = {
#     'db': 1
# }

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
