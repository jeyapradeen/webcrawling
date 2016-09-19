# -*- coding: utf-8 -*-
import scrapy
from passist.items import GoldPriceItem


class GoldSpider(scrapy.Spider):
    name = "gold"
    allowed_domains = ["goldpriceindia.com"]
    start_urls = (
        'http://www.goldpriceindia.com/gold-price-bangalore.php',
    )

    def parse(self, response):
    	item = GoldPriceItem()
        item["spider_name"]="gold"
    	item["site_url"] = response.url
        item["updated_date"] = response.xpath('//div[contains(@class,"dte")]/text()').extract()[0]
        item["title_text"]= response.xpath('//div[contains(@class,"hdn")]/text()').extract()[0]
        price_list = response.xpath('//div[@class="r1"]/b/text()').extract()
        item["one_gm_24_carat"] = price_list[0]
        item["one_gm_22_carat"] = price_list[2]
        yield item


        
