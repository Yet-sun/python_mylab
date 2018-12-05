"""爬虫模块"""

from urllib import request  # 模拟Http请求的Python内置库
import re  # 导入正则表达式模块


class Spider:
    """爬虫模块类"""
    url = 'https://www.douyu.com/directory/game/jdqs'  # 类变量，要抓取的网页
    root_pattern = '<div class="mes">[\s\S]*?</div>'  # 根模式，匹配这个元素里面的所有内容,\s空白字符\S非空白字符,*无限多个字符，?非贪婪模式

    def __fetch_content(self):
        """私有方法，获取网页内容"""
        http = request.urlopen(Spider.url)
        html = http.read()  # bytes,实际上是字节码
        htmlstr = str(html, encoding='utf-8')  # 字节码转换为字符串，使用UTF-8编码
        return htmlstr

    def __analysis(self, html_content):  # 要点：定位标签一定要选好，要确定是不是唯一的，是不是包含所需要的信息
        """私有方法,分析网页内容，没有正则表达式解决不了的问题"""
        root_html = re.findall(Spider.root_pattern, html_content)
        pass

    def get_html(self):
        content = self.__fetch_content()
        self.__analysis(content)


spider = Spider()
spider.get_html()
