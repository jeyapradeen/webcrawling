# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
import logging

# class MongoDBPipeline(object):

#     def __init__(self):
#         connection = pymongo.MongoClient(
#             settings['MONGODB_SERVER'],
#             settings['MONGODB_PORT']
#         )
#         db = connection[settings['MONGODB_DB']]
#         self.collection = db[settings['MONGODB_COLLECTION']]


class MongoDBPipeline(object):
    

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self.db = connection[settings['MONGODB_DB']]

    def process_item(self, item, spider):
        if spider.name == 'thehindu':
            collection = self.db[settings['MONGODB_COLLECTION']]
            valid = True
            for data in item:
                if not data:
                    valid = False
                    raise DropItem("Missing {0}!".format(data))
            if valid:
                if self.Is_Exists(collection,{"spider_name" : "thehindu"}):
                    collection.update({"spider_name" : "thehindu"},dict(item))
                else:
                    collection.insert(dict(item)) 
                logging.log(logging.INFO,"data added to MongoDB database!")
            return item
        elif spider.name == 'dictionary':
            collection = self.db[settings['MONGODB_COLLECTION']]
            valid = True
            for data in item:
                if not data:
                    valid = False
                    raise DropItem("Missing {0}!".format(data))
            if valid:
                if self.Is_Exists(collection,{"spider_name" : "dictionary"}):
                    collection.update({"spider_name" : "dictionary"},dict(item))
                else:
                    collection.insert(dict(item)) 
                logging.log(logging.INFO,"data added to MongoDB database!")
            return item
        elif spider.name == 'currency':
            collection = self.db[settings['MONGODB_COLLECTION']]
            valid = True
            for data in item:
                if not data:
                    valid = False
                    raise DropItem("Missing {0}!".format(data))
            if valid:
                if self.Is_Exists(collection,{"spider_name" : "currency"}):
                    collection.update({"spider_name" : "currency"},dict(item))
                else:
                    collection.insert(dict(item))      
                logging.log(logging.INFO,"data added to MongoDB database!")
            return item
        elif spider.name == 'gold':
            collection = self.db[settings['MONGODB_COLLECTION']]
            valid = True
            for data in item:
                if not data:
                    valid = False
                    raise DropItem("Missing {0}!".format(data))
            if valid:
                if self.Is_Exists(collection,{"spider_name" : "gold"}):
                    collection.update({"spider_name" : "gold"},dict(item))
                else:
                    collection.insert(dict(item)) 
                logging.log(logging.INFO,"data added to MongoDB database!")
            return item
        elif spider.name == 'quote':
            collection = self.db[settings['MONGODB_COLLECTION']]
            valid = True
            for data in item:
                if not data:
                    valid = False
                    raise DropItem("Missing {0}!".format(data))
            if valid:
                if self.Is_Exists(collection,{"spider_name" : "quote"}):
                    collection.update({"spider_name" : "quote"},dict(item))
                else:
                    collection.insert(dict(item)) 
                logging.log(logging.INFO,"data added to MongoDB database!")
            return item
        elif spider.name == 'vegprice':
            collection = self.db[settings['MONGODB_COLLECTION']]
            valid = True
            for data in item:
                if not data:
                    valid = False
                    raise DropItem("Missing {0}!".format(data))
            if valid:
                if self.Is_Exists(collection,{"spider_name" : "vegprice"}):
                    collection.update({"spider_name" : "vegprice"},dict(item))
                else:
                    collection.insert(dict(item)) 
                logging.log(logging.INFO,"data added to MongoDB database!")
            return item
    def Is_Exists(self,collection,spiderName):
        is_exists = collection.find_one(spiderName)
        if is_exists == None:
            return False
        else:
            return True


            
