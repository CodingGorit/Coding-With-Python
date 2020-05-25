#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 02 requests get.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 19:47

'''
    target: 发送 get 请求，并携带参数
'''

import requests

url = "http://httpbin.org/get"

# 不建议这样使用
url_get_params = "http://httpbin.org/get?name=geeg&age=25"

data = {
    "name":"coco",
    "age":18
}

# 使用 params 实现 get 请求传参
r = requests.get(url, params=data)
print(r.text) # 直接获取网页的信息

# print(r.json())  # 如果服务器 返回的 是 json 数据，用这个方法解析
