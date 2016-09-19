# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

class TamilsongsSpider(scrapy.Spider):
    name = "tamilsongs"
    allowed_domains = ["isaithenral.com"]
    start_urls = (
        'http://www.isaithenral.com/tamil-mp3-songs.php/',
    )

    def __init__(self, movie_name=None, year=None, *args, **kwargs):
        super(TamilsongsSpider, self).__init__(*args, **kwargs)
        self.movie_name = movie_name 
        self.movie_year = year

    def parse(self, response):
        regex_year=r'^.*%s.*$'%self.movie_year
        movie_relesed_year_url = response.xpath('//div[contains(@class,"col-1")]//a[contains(@href, "http:")]/@href').re(regex_year)
        print movie_relesed_year_url
        yield scrapy.Request(movie_relesed_year_url[0], callback=self.find_movie)
    def find_movie(self, response):
        regex_movie_name=r'^.*%s.*$'%self.movie_name
        movie_link = response.xpath('//a[contains(@href, "index.php?")]/@href').re(regex_movie_name)
        base_url = get_base_url(response)
        print base_url
        movie_link = urljoin_rfc(base_url, movie_link[0]) 
        print movie_link
        yield scrapy.Request(movie_link, callback=self.list_songs)
    def list_songs(self,response):
        base_url = get_base_url(response)
        movie_poster = response.xpath('//div[contains(@class,"cimgs")]/img/@src').extract()[0]
        print movie_poster
        songs = response.xpath('//td[contains(@class,"title stitle")]')
        for song in songs:
            print song.xpath("a/text()").extract()[0]
            print base_url+song.xpath("a/@href").extract()[0]
 
