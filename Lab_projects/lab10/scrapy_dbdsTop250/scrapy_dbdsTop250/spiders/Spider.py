# import scrapy
# from scrapy.http import Request
# from scrapy.selector import Selector
# from urllib.parse import urljoin
# # import json
# from scrapy_dbdsTop250.items import ScrapyDbdstop250Item
#
#
# class Spider(scrapy.Spider):
#     name = 'douBanReadingSpider'
#     allowed_domains = ["www.douban.com"]
#     # base_url = 'https://book.douban.com/top250'
#     # page = 1
#     # start_urls = [base_url + str(page)]
#     start_urls = ['https://book.douban.com/top250']
#
#     # def parse(self, response):
#         # data_list = json.loads(response.body)['data']['rl']
#         # pageNumber = json.loads(response.body)['data']['pgcnt']
#         #
#         # if pageNumber == Spider.page:
#         #     return
#         #
#         # for data in data_list:  # 循环获取每一个主播信息
#         #     item = ScrapyDbdstop250Item()
#         #     item['name'] = data['nn']
#         #     item['title'] = data['rn']
#         #     item['number'] = data['ol']
#         #     yield item
#         #
#         # Spider.page += 1
#         # url = Spider.base_url + str(Spider.page)
#         # yield scrapy.Request(url, callback=self.parse, dont_filter=True)  # dont_filter是停止内部过滤
#
#     def parse(self, response):
#         # 请求第一页
#         yield scrapy.Request(response.url, callback=self.parse_next)
#
#         # 请求其它页
#         for page in response.xpath('//div[@class="paginator"]/a'):
#             link = page.xpath('@href').extract()[0]
#             yield scrapy.Request(link, callback=self.parse_next)
#
#     def parse_next(self, response):
#         for item in response.xpath('//tr[@class="item"]'):
#             book = ScrapyDbdstop250Item()
#             book['title'] = item.xpath('td[2]/div[1]/a/@title').extract()[0]
#             book['price'] = item.xpath('td[2]/p/text()').extract()[0]
#             book['ratingNums'] = item.xpath('td[2]/div[2]/span[2]/text()').extract()[0]
#             yield book


import scrapy
import json
from Scrapy_dbdsTop250.items import ScrapyDbdstop250Item


class Spider(scrapy.Spider):
    name = 'douBanReadingSpider'
    allowed_domains = ["www.douban.com"]
    base_url = 'https://book.douban.com/top250'
    page = 1
    start_urls = [base_url + str(page)]
    # start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        data_list = json.loads(response.body)['data']['rl']
        pageNumber = json.loads(response.body)['data']['pgcnt']

        if pageNumber == Spider.page:
            return

        for data in data_list:  # 循环获取每一个主播信息
            item = ScrapyDbdstop250Item()
            item['name'] = data['nn']
            item['title'] = data['rn']
            item['number'] = data['ol']
            yield item

        Spider.page += 1
        url = Spider.base_url + str(Spider.page)
        yield scrapy.Request(url, callback=self.parse, dont_filter=True)  # dont_filter是停止内部过滤

