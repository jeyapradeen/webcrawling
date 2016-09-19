# -*- coding: utf-8 -*-
import scrapy
from passist.items import TheHinduItem

class ThehinduSpider(scrapy.Spider):
    name = "thehindu"
    allowed_domains = ["thehindu.com"]
    start_urls = (
        'http://www.thehindu.com/',
    )

    def parse(self, response):
    	url = response.xpath('//div[contains(@class, "h-main-lead posRel")]/h1/a/@href').extract()[0]
    	yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
    	item = TheHinduItem()
        item["spider_name"]="thehindu"
    	item['site_url'] = response.url
    	item['updated_date'] = response.xpath('//div[contains(@class,"artPubUpdate")]/text()').extract()[0]
    	item['title_text'] = response.xpath('//h1[contains(@class,"detail-title")]/text()').extract()[0]
    	item['image_url'] = response.xpath('//div[@id="pic"]/img/@src').extract()[0]
    	item['content_text']=response.xpath('//p/text()').extract_first()
        #print response.xpath('//p/text()').extract_first()
        # for sel in response.xpath('//p'):
        #     print sel.xpath('text()').extract().first()
        #     item['content_text'].append("<p>"+sel.xpath('text()').extract()[0]+"</p>")
        yield item



