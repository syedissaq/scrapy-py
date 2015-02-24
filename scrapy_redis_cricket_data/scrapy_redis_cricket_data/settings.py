# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_redis_cricket_data project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_redis_cricket_data'

SPIDER_MODULES = ['scrapy_redis_cricket_data.spiders']
NEWSPIDER_MODULE = 'scrapy_redis_cricket_data.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_redis_cricket_data (+http://www.yourdomain.com)'
# enables scheduling storing requests queue in redis
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# don't cleanup redis queues, allows to pause/resume crawls
SCHEDULER_PERSIST = True

# store scraped item in redis for post-processing
ITEM_PIPELINES = [
'scrapy_redis.pipelines.RedisPipeline',
]