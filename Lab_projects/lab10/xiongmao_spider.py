from urllib import request  # 模拟Http请求的Python内置库
import re  # 正则表达式模块


class Spider():
    """
        爬取熊猫TV 网站剑网三游戏分类下面所有主播的人气排行
    """
    url = 'https://www.panda.tv/cate/jxol3?pdt=1.24.s1.24.51fa92l7974'  # 类变量，要抓取的网页：豆瓣读书Top250

    # 定义所需的正则匹配模式
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):  # 抓取器
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
            # 利用正则将定位标签里获取的数据再次匹配, 提取出用户名和观看人数
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)

            # 将用户名和观看人数组装成字典
            anchor = {"name": name, "number": number}
            anchors.append(anchor)
        return anchors

    def __refine(self, anchors):
        """私有方法，精炼方法，去除空白字符"""
        l = lambda anchor: {'name': anchor['name'][0].strip(),
                            'number': anchor['number'][0].strip()
                            }
        return map(l, anchors)  # 遍历每个元素,返回map对象

    def __sort(self, anchors):
        """私有方法，按照评分排序"""
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)  # 倒序排列(高到低)
        return anchors

    def __sort_seed(self, anchor):
        """排序依据"""
        r = re.findall("\d*", anchor["number"])
        number = float(r[0])
        if "万" in anchor["number"]:
            number *= 10000
        return number

    def __show(self, anchors):
        """根据排序结果输出"""
        for rank in range(0, len(anchors)):
            print("rank %s: %s    %s" % (rank + 1, anchors[rank]["name"], anchors[rank]["number"]))

    def get_html(self):
        content = self.__fetch_content()
        # content=self.totalUrl()
        anchors = self.__analysis(content)
        refine_anchors = list(self.__refine(anchors))
        sorted_anchors = self.__sort(refine_anchors)
        self.__show(sorted_anchors)


spider = Spider()
spider.get_html()
