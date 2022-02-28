import scrapy

class FirstSpider(scrapy.Spider):
    #爬虫文件的名称:就是爬虫原文件的唯一标识
    name = 'first'
    #允许的域名:用来限定strat_urls的列表中哪些url可以进行请求发送
    allowed_domains = ['www.xxx.com']
    #起始的url列表:该列表中存放的url会被scrapy字典进行请求的发送
    start_urls = ['https://github.com/ShuyaoLim']
    #用作数据解析:response参数表示的就是请求成功后的响应对象
    def parse(self, response):
        print(response)
