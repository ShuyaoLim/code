# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from redis import Redis
class MovieproPipeline:
    conn=None
    def open_spider(self,spider):
        self.conn=self.conn
    def process_item(self, item, spider):
        dic={
            'name':item['name'],
            'desc':item['desc']
        }
        print(dic)
        self.conn.lpush('movieData',dic)
        return item
