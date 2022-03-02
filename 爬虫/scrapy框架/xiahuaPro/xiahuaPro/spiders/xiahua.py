import scrapy


class XiahuaSpider(scrapy.Spider):
    name = 'xiahua'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.7dapei.com/tuku/zhuanti/xiaohua.html']

    def parse(self, response):
        pass
