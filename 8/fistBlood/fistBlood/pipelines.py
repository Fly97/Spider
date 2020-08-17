# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class FistbloodPipeline:
    fp = None
    def open_spider(self, spider):
        print('开始爬虫')
        self.fp = open('./qiushi.txt', 'w', encoding='utf-8')

    # 处理item,接受一次调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ':' + content + '\n')
        return item

    def close_spider(self, spider):
        print('爬虫结束！！')
        self.fp.close()


class MymongoPileLine:
    conn = None
    mydb = None
    mytable = None

    def open_spider(self, spider):
        print('开始入库！！')
        self.conn = pymongo.MongoClient("mongodb://localhost:27017")
        self.mydb = self.conn['scrapy']

    def process_item(self, item, spider):
        try:
            self.mytable = self.mydb['qiushi']
            dic = {
                'author': item['author'],
                'content': item['content']
            }
            self.mytable.insert_one(dic)
        except Exception as e:
            print(e)
        return item

    def close_spider(self, spider):
        print('已经入MonGoDB库！！')
