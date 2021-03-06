import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']
    models_urls=[] #存详情页url
    def __init__(self):
        self.bro=webdriver.Chrome(executable_path='/Users/shuyao/Desktop/code/爬虫/动态加载数据处理/chromedriver')
    def parse(self, response):
        li_list=response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        alist=[2,3,5,6,8]
        for index in alist:
            model_url=li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)
        #依次对每一个板块对应的页面进行请求
        for url in self.models_urls:  #对每个板块的url进行请求发送
            yield scrapy.Request(url,callback=self.parse_model)

    def parse_model(self,response):#解析每一个板块页面对应新闻的标题和新闻页面的url
        div_list=response.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div/ul/li/div')
        for div in div_list:
            title=div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url=div.xpath('./div/div[1]/h3/a/@href').extract_first()
            item=WangyiproItem()
            item['title']=title

            yield scrapy.Request(url=new_detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self,response):
        content=response.xpath('//*[@id="content"]').extract()
        content=''.join(content)
        item=response.meta['item']
        item['content']=content
        yield item

    def closed(self,spider):
        self.bro.quit()

