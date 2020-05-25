#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 04 requests cookie.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/18 23:17

'''
    target: requests 高级用法 Cookies
'''

import requests
url = "http://www.baidu.com"

r = requests.get(url)

print(r.cookies)

# 遍历输出每一个 cookie 的键值对
for key, value in r.cookies.items():
    print(key + '=' + value)