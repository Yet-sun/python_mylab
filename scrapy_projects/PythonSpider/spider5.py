"""爬虫模块"""

from urllib import request  # 模拟Http请求的Python内置库
import re  # 导入正则表达式模块
from pprint import pprint


class Spider:
    """爬虫模块类"""
    url = 'https://www.douyu.com/directory/game/jdqs'  # 类变量，要抓取的网页
    root_pattern = '<div class="mes">([\s\S]*?</div>[\s\S]*?)</div>'  # 用组，去除最外层DIV
    title_pattern = '<h3 class="ellipsis">([\s\S]*?)</h3>'  # 直播标题名称正则表达式
    name_pattern = '<span class="dy-name ellipsis fl">([\s\S]*?)</span>'  # 主播名称正则表达式
    number_pattern = '<span class="dy-num fr"  >([\s\S]*?)</span>'  # 直播人数正则表达式

    def __fetch_content(self):
        """私有方法，获取网页内容"""
        http = request.urlopen(Spider.url)
        html = http.read()  # bytes,实际上是字节码
        htmlstr = str(html, encoding='utf-8')  # 字节码转换为字符串，使用UTF-8编码
        return htmlstr

    def __analysis(self, html_content):  # 要点：定位标签一定要选好，要确定是不是唯一的，是不是包含所需要的信息
        """私有方法,分析网页内容，没有正则表达式解决不了的问题"""
        root_html = re.findall(Spider.root_pattern, html_content)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            title = re.findall(Spider.title_pattern, html)
            anchor = {'title': title, 'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    def __refine(self, anchors):
        """私有方法，精炼方法，去除空白字符"""
        l = lambda anchor: {'title': anchor['title'][0].strip(),
                            'name': anchor['name'][0].strip(),
                            'number': anchor['number'][0].strip()
                            }
        return map(l, anchors)  # 遍历每个元素,返回map对象

    def get_html(self):
        content = self.__fetch_content()
        anchors = self.__analysis(content)
        refine_anchors = list(self.__refine(anchors))
        pprint(refine_anchors)  # 按人气排序


spider = Spider()
spider.get_html()
