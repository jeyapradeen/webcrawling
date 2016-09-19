# -*- coding: utf-8 -*-
import scrapy


class WikiSpider(scrapy.Spider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = (
        'https://en.wikipedia.org/wiki/Main_Page',
    )

    def parse(self, response):
        print  "title = "+response.xpath('//span[@id="From_today.27s_featured_article"]/text()').extract()[0]
        print  "img_url = https:"+response.xpath('.//*[@id="mp-tfa-img"]/div/a/img/@src').extract()[0]

