#!/usr/bin/env python

# operator:Dean
# time:2017-11-19
# function:实现静态页面的图片的爬取

import requests
import re
import urllib

head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'}
url = 'https://www.qiushibaike.com/imgrank/page/'
x = 1
for i in range(1, 13):
    url = url + str(i) + '/'
    page = requests.get(url, headers=head)
    ren = re.compile(r'class="thumb".*?<img src="(.*?)" alt=".*?</a>\n</div>', re.S)
    buff = re.findall(ren, page.text)
    for each_buff in buff:
        each_buff = 'https:' + each_buff
        urllib.request.urlretrieve(each_buff, './picture/%d.jpg' % x)
        print('爬取图片:', each_buff)
        x = x + 1
print('本次爬取一共爬取%d张图片' % x)
