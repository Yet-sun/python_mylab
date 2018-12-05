from urllib import request  # 模拟Http请求的Python内置库
import re  # 正则表达式模块
from pprint import pprint


class Spider():
    url = 'https://book.douban.com/top250'  # 类变量，要抓取的网页：豆瓣读书Top250

    # root_pattern = '<td valign="top">[\s\S]*?</td>'  # 根模式，匹配这个元素里面的所有内容,\s空白字符\S非空白字符,*无限多个字符，?非贪婪模式
    root_pattern = '<td valign="top">([\s\S]*?</td>[\s\S]*?)</td>'  # 用组，去除最外层td
    title_pattern = re.compile(r'(?<=&#34; title=").*?(?=")')
    # title_pattern = '(?<=&quot;" title=").*?(?=")([\s\S]*?)</a>'  # .*?表示满足条件的尽量少的任意字符,(?=")表示后缀为"
    author_pattern = '<p class="pl">([\s\S]*?)</p>'
    ratingNums_pattern = '<span class="rating_nums">([\s\S]*?)</span>'
    commentary_pattern = '<span class="inq">([\s\S]*?)</span>'

    # def totalUrl(self):
    #     urls=[self.url+'?start={}'.format(i) for i in range(1,11)]
    #     for url in urls:
    #         print("正在获取："+url.split('/')[-2]+"页")
    #         self.__fetch_content(url)


    # def __fetch_content(self,url):  # 抓取器
    def __fetch_content(self):
        """私有方法，获取网页内容"""
        # http = request.urlopen(url)
        http = request.urlopen(Spider.url)
        html = http.read()  # bytes,实际上是字节码
        htmlstr = str(html, encoding='utf-8')  # 字节码转换为字符串，使用UTF-8编码
        return htmlstr

    def __analysis(self, html_content):  # 分析器
        # 要点：定位标签一定要选好，要确定是不是唯一的，是不是包含所需要的信息
        root_html = re.findall(Spider.root_pattern, html_content)
        anchors = []
        for html in root_html:
            title = re.findall(Spider.title_pattern, html)
            author = re.findall(Spider.author_pattern, html)
            ratingNums = re.findall(Spider.ratingNums_pattern, html)
            commentary = re.findall(Spider.commentary_pattern,html)
            anchor = {'title': title, 'author': author, 'ratingNums': ratingNums,'commentary':commentary}
            anchors.append(anchor)
        # pprint(anchors)
        return anchors

    def __refine(self, anchors):
        """私有方法，精炼方法，去除空白字符"""
        l = lambda anchor: {'title': anchor['title'][0].strip(),
                            'author': anchor['author'][0].strip(),
                            'ratingNums': anchor['ratingNums'][0].strip(),
                            'commentary':anchor['commentary'][0].strip()
                            }
        return map(l, anchors)  # 遍历每个元素,返回map对象

    def __sort(self, anchors):
        """私有方法，按照评分排序"""
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)  # 倒序排列(高到低)
        return anchors

    def __sort_seed(self, anchor):
        """排序依据"""
        return anchor['ratingNums']

    def __show(self, anchors):
        """根据排序结果输出"""
        for anchor in anchors:
            print(anchor['title'] + '-----' + anchor['ratingNums'] + '分-----' + anchor['author'] + '-----' + anchor['commentary'])

    def get_html(self):
        content = self.__fetch_content()
        # content=self.totalUrl()
        anchors = self.__analysis(content)
        refine_anchors = list(self.__refine(anchors))
        sorted_anchors = self.__sort(refine_anchors)
        self.__show(sorted_anchors)


spider = Spider()
spider.get_html()
