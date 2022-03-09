import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = 'sun'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest']
    #链接提取器:根据指定规则(allow="正则")进行指定链接的提取
    link=LinkExtractor(allow=r'type=4$page=\d+')
    rules = (
        #规则解析器:
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
      print(response)

