# -*- coding: utf-8 -*-
import scrapy
import re
from demo1.items import Demo1Item

class TSpider(scrapy.Spider):
    name = 't'
    dynamic_domain = '551ci.com'
    allowed_domains = [dynamic_domain]
    start_urls =[]
    #for i in range(21,30):
    for i in range(11,13):
       #start_urls.append('https://www.'+dynamic_domain+'/html/news/69/')
       start_urls.append('https://www.'+dynamic_domain+'/html/news/69/'+ str(i)+'.html')
       #start_urls.append('https://www.'+dynamic_domain+'/html/news/7/')
       
    def parse(self, response):
        list = response.css('.video-pic')
        #i = request.meta['i']
        url = response.url
        pages = re.findall(r"/news/69/(.+?).html",url)
        if(len(pages)):
            i = pages[0]
        else:
            i = 'f'
        prefix = 'https://www.' + self.dynamic_domain
        for img in list:
            imgname = img.css('a::attr(title)').extract_first()
            imgUrl = img.css('a::attr(href)').extract_first()
            print(imgname,imgUrl)
            imgUrl = prefix + imgUrl + "?i=" + i
            yield scrapy.Request(imgUrl, callback=self.content)
    
    
    def content(self, response):
        item = Demo1Item()
        url = response.url
        i = (re.findall(r"i=(.+?)$",url))[0]
        item['name'] = response.css(".news_details h1::text").extract_first()
        item['imgUrl'] = response.css(".details-content p img::attr(src)").extract()
        item['i'] =  "page_"+i
        yield item
