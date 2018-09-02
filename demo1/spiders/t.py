# -*- coding: utf-8 -*-
import scrapy
from demo1.items import Demo1Item

class TSpider(scrapy.Spider):
    name = 't'
    dynamic_domain = '8886jj.com'
    allowed_domains = [dynamic_domain]
    start_urls =[]
    #for i in range(21,30):
    for i in range(1):
        #start_urls.append('https://www.'+dynamic_domain+'/Html/63/index-'+ str(i+1)+'.html')
        start_urls.append('https://www.'+dynamic_domain+'/Html/63/index.html')
    
    def parse(self, response):
        list = response.css('li')
        prefix = 'https://www.' + self.dynamic_domain
        for img in list:
            imgname = img.css('a::text').extract_first()
            imgUrl = img.css('a::attr(href)').extract_first()
            imgUrl = prefix + imgUrl 
            #print(imgname,imgUrl)
            yield scrapy.Request(imgUrl, callback=self.content)
    
    
    def content(self, response):
        item = Demo1Item()
        item['name'] = response.css(".page_title h1::text").extract_first()
        item['imgUrl'] = response.css(".content font img::attr(src)").extract()
        yield item
