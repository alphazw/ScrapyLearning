# -*- coding: utf-8 -*-
'''
Author: Andy
Date:2016年7月21日
for spide top250 of douban movie
代码很糙，谨慎观看。
'''

from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor

from DoubanMovie.items import DoubanmovieItem

class DoubanMovieSpider(CrawlSpider):
    name = "doubantop250"
    allowed_domains=["douban.com"]

    #以下是靠网页抓取进行爬取，有一些小问题
    start_urls=[
        'https://movie.douban.com/top250'
    ]
    rules = (
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/top250\?start=\d+.*?')), callback='parse_item',
             follow=True),
    )
    #问题：输出有一部分超出索引？why？
    # 答案：找到症结：由于存在有些电影没有评论，导致quote输出超索引


    #下面使用starturl的规律进行爬取
    #start_urls = []
    #for i in range(0,250,25):
    #    start_urls.append(
    #        'https://movie.douban.com/top250?start=%d&filter=' % i
    #    )


    def parse_item(self, response):
        #print 'response:'
        #print response
        item=DoubanmovieItem()
        sel=Selector(response)
        #/ html / body / div[3] / div[1] / div / div[1] / ol / li[1] / div / div[2] / div[1] / a
        movie_url=sel.xpath('//li/div/div/div/a/@href').extract()
        #print movie_url
        movie_num=sel.xpath('//div[@class="pic"]/em/text()').extract()
        movie_name=sel.xpath('//a/span[1][@class="title"]/text()').extract()
        movie_star=sel.xpath('//span[@class="rating_num"]/text()').extract()
        #movie_quote=sel.xpath('//p[@class="quote"]/span[@class="inq"]/text()').extract()
        #print 'movie_name:'
        #print movie_name
        item['num']=[n.encode('utf-8') for n in movie_num]
        item['url']=[n.encode('utf-8') for n in movie_url]
        item['name']=[n.encode('utf-8')  for n in movie_name]
        item['star']=[n.encode('utf-8')  for n in movie_star]
        #item['quote']=[n.encode('utf-8')  for n in movie_quote]

        yield item