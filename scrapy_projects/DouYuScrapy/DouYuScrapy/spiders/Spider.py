import scrapy
import json
from DouYuScrapy.items import DouyuItem


class Spider(scrapy.Spider):
    name = 'douyuSpider'
    allowed_domains = ["www.douyu.com"]
    base_url = 'https://www.douyu.com/gapi/rkc/directory/2_270/'
    page = 1
    start_urls = [base_url + str(page)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']['rl']
        pageNumber = json.loads(response.body)['data']['pgcnt']

        if pageNumber == Spider.page:
            return

        for data in data_list:  # 循环获取每一个主播信息
            item = DouyuItem()
            item['name'] = data['nn']
            item['title'] = data['rn']
            item['number'] = data['ol']
            yield item

        Spider.page += 25
        url = Spider.base_url + str(Spider.page)
        yield scrapy.Request(url, callback=self.parse, dont_filter=True) #dont_filter是停止内部过滤


