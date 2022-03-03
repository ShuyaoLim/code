import scrapy
from bossPro.items import BossproItem
class BossSpider(scrapy.Spider):
    name = 'boss'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101020100&industry=&position=']
    url='https://www.zhipin.com/job_detail/?query=python&page=%d'
    page_num=2
    def parse_detail(self,response):
        item=response.meta['item']
        job_desc=response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc=''.join(job_desc)
        #print(job_desc)
        item['job_desc']=job_desc
        yield item
    def parse(self, response):
        li_list=response.xpath('//*[@id="main"]/div/div[3]/ul')
        for li in li_list:
            item=BossproItem()
            job_name=li.xpath('.//div[@class="info-primary"]//p/text()').extract_first
            item['job_name']=job_name
            #print(job_name)
            detail_url='https://www.zhipin.com/'+li.xpath('.//div[@class="info-primary"]/a/@href').extract_first
            #对详情页发请求获取详情页面源码数据
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        #分页操作
        if self.page_num<=3:
            new_url=format(self.url%self.page_num)
            self.page_num+=1
            yield scrapy.Request(new_url,callback=self.parse)
