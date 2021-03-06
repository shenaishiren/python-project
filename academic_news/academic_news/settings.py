# -*- coding: utf-8 -*-

# Scrapy settings for academic_news project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'academic_news'
DEPTH_LIMIT = 1
DOWNLOAD_DELAY = 0.15  # 150ms

MONGO_URI = "localhost"
MONGO_PORT = 27017
MONGO_DB = "academic_news"
DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'
# DUPEFILTER_CLASS = "news.mydupfilter.SeenURLFilter"
LOG_FILE = "academic_news.log"
LOG_STDOUT = True

SPIDER_MODULES = ['academic_news.spiders']
NEWSPIDER_MODULE = 'academic_news.spiders'

ITEM_PIPELINES = {
    'academic_news.pipelines.AcademicNewsPipeline': 300,
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'academic_news (+http://www.yourdomain.com)'
