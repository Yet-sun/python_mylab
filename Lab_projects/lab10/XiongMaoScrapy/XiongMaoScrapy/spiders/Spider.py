import scrapy
import json
from XiongMaoScrapy.items import XiongmaoscrapyItem


class Spider(scrapy.Spider):
    name = 'xiongmaoSpider'
    allowed_domains = ["www.panda.tv"]
    base_url = 'https://www.panda.tv/ajax_sort?token=&pageno='
    other_url = '&pagenum=120&classification=jxol3&order=top&_=152993276674'
    other_num = '7'
    page = 1
    start_urls = [base_url + str(page) + other_url + str(other_num)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']['items']
        # pageNumber = json.loads(response.body)['data']['pgcnt']
        #
        # if pageNumber == Spider.page:
        #     return

        for data in data_list:  # 循环获取每一个主播信息
            item = XiongmaoscrapyItem()
            item['title'] = data['name']
            item['id'] = data['id']
            item['number'] = data['person_num']
            yield item

        Spider.page += 1
        url = Spider.base_url + str(Spider.page) + Spider.other_url + str(Spider.other_num)
        yield scrapy.Request(url, callback=self.parse, dont_filter=True)  # dont_filter是停止内部过滤
