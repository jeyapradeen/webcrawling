# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from passist.items import CurrencyItem


class CurrencySpider(scrapy.Spider):
    name = "currency"
    allowed_domains = ["dollars2rupees.com"]
    start_urls = (
        'http://www.dollars2rupees.com/',
    )

    def parse(self, response):
        item = CurrencyItem()
        item["spider_name"]="currency"
        item['site_url'] = response.url
        item['title_text'] = response.xpath('//h2[contains(@class,"panel-title")]/text()').extract()[0]
        US_to_IN_label = response.xpath('//span[@id="ratesC1Label"]/text()').extract()[0]
        US_to_IN_value = response.xpath('//span[@id="ratesC1Value"]/text()').extract()[0]
        IN_to_US_label = response.xpath('//span[@id="ratesC2Label"]/text()').extract()[0]
        IN_to_US_value = response.xpath('//span[@id="ratesC2Value"]/text()').extract()[0]
        #print response.xpath('.//*[@id="ratesUpdatedLink"]/@href').extract()[0] ## for updated date
        item['US_to_IN'] = US_to_IN_label + US_to_IN_value
        item['IN_to_US'] = IN_to_US_label + IN_to_US_value
        yield item

        

        
