#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 02 requests post.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 20:03

'''
    target：post 请求，并携带参数
'''
import requests

data = {
    "name":"coco",
    "age":25
}

r = requests.post("http://httpbin.org/post", data=data)

print(r.text)