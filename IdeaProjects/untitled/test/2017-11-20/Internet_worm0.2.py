#!/usr/bin/env python

# operator:Dean
# time:2017-11-19
# function:实现ajax加载页面的图片的爬取

import json
import urllib.request
import requests
import datetime

keyword = 'beautiful_girl'


def url_operate(my_num):
    # 地址
    url = 'https://www.toutiao.com/search_content/?offset=%d&format=json&keyword=美女&autoload=true&count=20&cur_tab=1'
    # 头部信息
    head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'}
    # 发出请求
    response = requests.get(url % my_num, headers=head)
    # 将请求转换为json
    response = json.loads(response.text)
    data = response["data"]
    # 获取响应中的data
    return data


def get_image(my_data):
    for i in my_data:
        image_list = i["image_detail"]
        for image_url_list in image_list:
            image_url = image_url_list["url"]
            print(str(datetime.datetime.now()) + '正在爬取:' + image_url)
            urllib.request.urlretrieve(image_url, './picture/%s' % str(datetime.datetime.now()))
    return 0


if __name__ == '__main__':
    for offset in range(20, 200, 20):
        data = url_operate(offset)
        get_image(data)
