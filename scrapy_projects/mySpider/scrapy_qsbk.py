# -*- coding:utf-8 -*-

import urllib.request

page =1
url = 'http://qiushibaike.com/hot/page' + str(page)
user_agent = 'Mozilla/4.0(Compatible; MSIE 5.5;Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib.request(url, headers=headers)
    response = urllib.request.urlopen(request)
    print(response.read())
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)


