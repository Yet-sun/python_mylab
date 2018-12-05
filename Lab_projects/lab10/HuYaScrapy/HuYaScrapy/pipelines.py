# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class HuyascrapyPipeline(object):
    file_name = 'D:\\IDE\\result.csv'

    def process_item(self, item, spider):
        item = dict(item)
        if not os.path.exists(HuyascrapyPipeline.file_name):  # 文件不存在先创建，然后输入表头
            with open(HuyascrapyPipeline.file_name, "x") as f:
                f.write('title,')
                f.write('name,')
                f.write('number')
                f.write('\n')  # ‘\n’ 表示换行
                f.close()
        with open(HuyascrapyPipeline.file_name, "a+") as f:
            f.write(item['title'] + ',')
            f.write(item['name'] + ',')
            f.write(str(item['number']))
            f.write('\n')  # ‘\n’ 表示换行
            f.close()
