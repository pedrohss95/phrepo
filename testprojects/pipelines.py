# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class TestprojectsPipeline:
    collection_name = 'new_project'
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://phsoares:zecamalu@cluster0.mk0mb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client['TEST']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[collection_name].insert(item)
        return item
