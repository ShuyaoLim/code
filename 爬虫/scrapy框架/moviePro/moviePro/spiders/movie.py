import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from moviePro.items import MovieproItem
class MovieSpider(CrawlSpider):
    name = 'movie'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.4567tv.net/vod-type-id-1-pg-1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/frim/index1-\d+\.html'), callback='parse_item', follow=True),
    )
    conn=Redis(host='127.0.0.1',port=6379)
    def parse_item(self, response):
        li_list=response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            detail_url='http://www.4567tv.net/'+li.xpath('./div/a/@href').extract_first()
            ex=self.conn.sadd('urls',detail_url)
            if ex==1:
                print('该url没有被爬过,可以进行数据爬取')
                yield scrapy.Request(url=detail_url,callback=self.parst_detail)
            else:
                print('数据没有更新,暂无新数据可爬取')
    def parst_detail(self,response):
        item=MovieproItem()
        item['name']=response.xpath('/html/body/div[1]/div/div/div/div[2]/h1/text()').extract
        item['desc']=response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]//text()')
        item['desc']=''.join(item['desc'])
        yield item
