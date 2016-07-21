# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class DoubanmoviePipeline(object):
    def __init__(self):
        self.file=codecs.open('douban_topmovie.json',mode='wb',encoding='utf-8')


    def process_item(self, item, spider):
        line='the top movie list: '+'\n'

        for i in range(len(item['name'])):

            movie_num={"num":item['num'][i]}
            movie_name={"movie_name":item['name'][i]}
            star={"star":item['star'][i]}
            #quote={"moive_quote":item['quote'][i]}
            url = {"movie_address": item['url'][i]}

            line = line + json.dumps(movie_num, ensure_ascii=False)
            line = line + json.dumps(movie_name,ensure_ascii=False)
            line = line + json.dumps(star, ensure_ascii=False)
            #line = line + json.dumps(quote, ensure_ascii=False)+"\n"
            line = line + json.dumps(url, ensure_ascii=False)+"\n"
        self.file.write(line)

    def close_spider(self,spider):
        self.file.close()
