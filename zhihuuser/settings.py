# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

# JOBDIR='pause'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'

MONGO_URI='localhost'
MONGO_DB='zhihuuser'

MY_USER_AGENT = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML like Gecko) Chrome/23.0.1271.95 Safari/537.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/31.0.1650.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.153 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.120 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML like Gecko) Chrome/23.0.1271.95 Safari/537.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML like Gecko) Chrome/26.0.1410.64 Safari/537.31',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.125 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.143 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/27.0.1453.110 Safari/537.36'
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
     'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML like Gecko) Chrome/23.0.1271.95 Safari/537.11',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/31.0.1650.63 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.153 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.120 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML like Gecko) Chrome/23.0.1271.95 Safari/537.11',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML like Gecko) Chrome/26.0.1410.64 Safari/537.31',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.125 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.143 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/27.0.1453.110 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/38.0.2125.111 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.103 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.114 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 1094) AppleWebKit/537.77.4 (KHTML like Gecko) Version/7.0.5 Safari/537.77.4',
     'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.120 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.153 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 1094) AppleWebKit/537.78.2 (KHTML like Gecko) Version/7.0.6 Safari/537.78.2',
     'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML like Gecko) Chrome/21.0.1180.89 Safari/537.1',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
     'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.143 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/31.0.1650.57 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.124 Safari/537.36',
     'Mozilla/5.0 (Windows NT 5.1; rv:16.0) Gecko/20100101 Firefox/16.0',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 712 like Mac OS X) AppleWebKit/537.51.2 (KHTML like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53'
     ]

# PROXIES=[
#    'http://139.196.104.28:9000',
#    'http://202.38.92.100:3128',
#    'http://125.77.25.123:80',
#    'http://115.154.63.223:8123',
#    'http://116.199.2.197:80',
#    'http://121.41.175.199:80',
# ]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
RANDOMIZE_DOWNLOAD_DELAY=True
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'en',
'host':'www.zhihu.com',
'Referer': 'http://www.zhihu.com',
'authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
}
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'zhihuuser.middlewares.MyUserAgentMiddleware': 400,
   # 'zhihuuser.middlewares.ProxyMiddleware':543,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihuuser.pipelines.MongoPipeline': 300,
'scrapy_redis.pipelines.RedisPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

SCHEDULER = "scrapy_redis.scheduler.Scheduler"

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

SCHEDULER_PERSIST = True

REDIS_URL = 'redis://120.78.52.93:redis@120.78.52.93:6379'
