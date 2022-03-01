import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text']

    # def parse(self, response):
    #     #解析:作者的名称+段子内容
    #     div_list=response.xpath('//div[@id="content-left"]/div')
    #     all_data=[]#存储所有解析的数据
    #     for div in div_list:
    #         author=div.xpath('.div[1]/a[2]/h2/text()')[0].extract()
    #         content=div.xpath('./a[1]/div/span//text()').extract()
    #         content=''.join(content)
    #         dic={
    #             'author':author,
    #             'content':content
    #         }
    #         all_data.append(dic)
    #         return all_data
    def parse(self, response):
        #解析:作者的名称+段子内容
        div_list=response.xpath('//div[@id="content-left"]/div')
        all_data=[]#存储所有解析的数据
        for div in div_list:
            author=div.xpath('.div[1]/a[2]/h2/text() ｜.div/[1]/span/h2/text()').extract_first()
            content=div.xpath('./a[1]/div/span//text()').extract()
            content=''.join(content)
            item=QiubaiproItem()
            item['author']=author
            item['content']=content

            yield item  #将item提交给管道