# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from passist.items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["brainyquote.com"]
    start_urls = (
        'http://www.brainyquote.com/quotes_of_the_day.html',
    )

    def parse(self, response):
        item = QuoteItem()
        item["spider_name"]="quote"
        item["site_url"] = response.url
        item["title_text"] = response.xpath('//div[contains(@class,"m_panel sticky_adzone")]/h1/text()').extract_first()
        item["img_url"] = "http://www.brainyquote.com" + response.xpath('//div[contains(@class,"m_panel sticky_adzone")]/div/a/img/@src').extract_first()
        yield item

