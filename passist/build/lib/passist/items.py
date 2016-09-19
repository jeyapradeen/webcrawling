# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TheHinduItem(scrapy.Item):
    # define the fields for your item here like:
    spider_name = scrapy.Field()
    site_url = scrapy.Field()
    updated_date = scrapy.Field()
    title_text = scrapy.Field()
    image_url =  scrapy.Field()
    content_text = scrapy.Field()

class DictionaryItem(scrapy.Item):
    # define the fields for your item here like:
    spider_name = scrapy.Field()
    site_url = scrapy.Field()
    updated_date = scrapy.Field()
    title_text = scrapy.Field()
    word_text = scrapy.Field()
    word_meaning =  scrapy.Field()

class CurrencyItem(scrapy.Item):
    # define the fields for your item here like:
    spider_name = scrapy.Field()
    site_url = scrapy.Field()
    title_text = scrapy.Field()
    US_to_IN = scrapy.Field()
    IN_to_US =  scrapy.Field()

class GoldPriceItem(scrapy.Item):
    # define the fields for your item here like:
    spider_name = scrapy.Field()
    site_url = scrapy.Field()
    updated_date = scrapy.Field()
    title_text = scrapy.Field()
    one_gm_24_carat = scrapy.Field()
    one_gm_22_carat =  scrapy.Field()

class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    spider_name = scrapy.Field()
    site_url = scrapy.Field()
    title_text = scrapy.Field()
    img_url = scrapy.Field()

class VegPriceItem(scrapy.Item):
    # define the fields for your item here like:
    spider_name = scrapy.Field()
    site_url = scrapy.Field()
    title_text = scrapy.Field()
    data = scrapy.Field()



