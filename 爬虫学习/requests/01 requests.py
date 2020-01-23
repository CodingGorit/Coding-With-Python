#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 01 requests.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/18 18:03

import requests

# 定义请求的 url
url = "http://www.baidu.com"

response = requests.get(url=url)

print(response)
print(response.text)
print(response.content.decode("utf-8"))
print(response.status_code)
print(response.headers)

print(response.request.headers) # 请求头信息
print(response.headers)
