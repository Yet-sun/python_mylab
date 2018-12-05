# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDbdstop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 书名
    author = scrapy.Field()  # 书的作者、出版社、价钱等信息
    ratingNums = scrapy.Field()  # 书评分
    commentary = scrapy.Field()  # 短评
