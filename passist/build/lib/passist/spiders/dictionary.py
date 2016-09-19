# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from passist.items import DictionaryItem


class DictionarySpider(scrapy.Spider):
    name = "dictionary"
    allowed_domains = ["dictionary.com"]
    start_urls = (
        'http://www.dictionary.com/wordoftheday/',
    )

    def parse(self, response):
        sel = Selector(response)
        item = DictionaryItem()
        item["spider_name"]="dictionary"
        item['site_url'] = response.url
        item['title_text'] = "Word of the Day"
        item["updated_date"] = sel.xpath('//div[contains(@class,"date-wrapper oneClick-disabled")]/span/text()').extract()[0]
        item["word_text"] = sel.xpath('//div[contains(@class,"definition-header")]/strong/text()').extract()[0]
        item["word_meaning"] = sel.xpath('//div[contains(@class,"definition-box")]/ol/li/span/text()').extract()[0]
        yield item



