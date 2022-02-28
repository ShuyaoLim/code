import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text']

    def parse(self, response):
        #解析:作者的名称+段子内容
        div_list=response.xpath('//div[@id="content-left"]/div')
        for div in div_list:
            author=div.xpath('.div[1]/a[2]/h2/text()')[0].extract()
            content=div.xpath('./a[1]/div/span//text()').extract()
            content=''.join(content)
            print(author,content)
            break