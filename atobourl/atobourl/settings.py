# -*- coding: utf-8 -*-

# Scrapy settings for atobourl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'atobourl'

SPIDER_MODULES = ['atobourl.spiders']
NEWSPIDER_MODULE = 'atobourl.spiders'
JOBDIR='company_messages'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'atobourl (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'atobourl.middlewares.AtobourlSpiderMiddleware': 543,
#}

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

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
        'atobourl.ProxyMidware.MyproxiesMidware': 541,
        'atobourl.multi_selenium.SeleniumMiddleware': 542,
        'atobourl.UseragentMidware.RandomUseragentMidware': 543, 
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
        }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'atobourl.pipelines.AtobourlPipeline': 300,
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
