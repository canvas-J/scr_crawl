# -*- coding: utf-8 -*-

BOT_NAME = 'plain'
SPIDER_MODULES = ['plain.spiders']
NEWSPIDER_MODULE = 'plain.spiders'
# JOBDIR = 'queue_dir'

ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False
CONCURRENT_REQUESTS = 30
# DOWNLOAD_DELAY = 2
# RANDOMIZE_DOWNLOAD_DELAY = True


DEFAULT_REQUEST_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        'Accept-Encoding': 'gzip'}

DOWNLOADER_MIDDLEWARES = {
        # 'plain.ProxyMidware.MyproxiesMidware': 210,
        # 'plain.multi_selenium.SeleniumMiddleware': 350,
        'plain.UseragentMidware.RandomUseragentMidware': 220, 
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
        }

# ITEM_PIPELINES = {
#    'plain.pipelines.OutputPipeline': 200,
# }


# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
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
