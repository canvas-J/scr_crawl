# -*- coding: utf-8 -*-

# Scrapy settings for jingdong project
BOT_NAME = 'jingdong'
SPIDER_MODULES = ['jingdong.spiders']
NEWSPIDER_MODULE = 'jingdong.spiders'
# JOBDIR = 'jd_items'

# 100页
KEYWORDS = ['洁面', '精华', '面膜', '乳液', '爽肤水', '男士洁面', '眼霜', '卸妆', '男士面膜', '男士乳液', '男士精华', '男士面霜', '男士洗发水', '素颜霜', '妆前乳', '身体乳', '男士爽肤水', '面部按摩仪']
# 65页
KEYWORDS = ['婴儿沐浴露', '喷雾', '漱口水', '男士遮瑕', '脱毛膏', '安瓶', '防晒']
# 35页
KEYWORDS = ['男士眼霜', '磨砂膏', '婴儿洗发水', '男士防晒', '修颜霜', '婴儿润肤乳液']
# 12页
KEYWORDS = ['婴儿按摩油', '面部按摩霜', '元气口红', '脱毛仪', '宝宝防晒露', '男士阴影']
# 测试
KEYWORDS = ['牙膏']
MAX_PAGE = 10

ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False
CONCURRENT_REQUESTS = 12
# DOWNLOAD_DELAY = 1
# RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_REQUESTS_PER_IP = 1


DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

DEFAULT_REQUEST_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Encoding': 'gzip'}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
        'jingdong.ProxyMidware.MyproxiesMidware': 100,
        'jingdong.multi_selenium.SeleniumMiddleware': 542,
        'jingdong.UseragentMidware.RandomUseragentMidware': 110, 
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

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'jingdong.pipelines.JingdongPipeline': 300,
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
