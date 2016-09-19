# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from passist.items import VegPriceItem

class VegpriceSpider(scrapy.Spider):
    name = "vegprice"
    allowed_domains = ["http://bestbengaluru.com/"]
    start_urls = (
        'http://bestbengaluru.com/vegetable-price-bangalore',
    )

    def parse(self, response):
    	item = VegPriceItem()
        item["spider_name"]="vegprice"
        item["site_url"] = response.url
        item["title_text"] = response.xpath("//h3/text()").extract_first()
    	sel = Selector(response)
    	vegs = sel.xpath("//div[contains(@class,'veg')]")
    	base_url = get_base_url(response)
    	data = []
        for veg in vegs:
        	relative_url= veg.xpath("img/@src").extract_first()
        	d=dict()
        	d["img_url"] = urljoin_rfc(base_url, relative_url)
        	d["veg_name"] = veg.xpath("h4/text()").extract_first()
        	d["veg_price"] = veg.xpath("h5/text()").extract_first()
        	data.append(d)
        item["data"] = data
        yield item




