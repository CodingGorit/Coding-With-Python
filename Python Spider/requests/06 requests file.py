#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 06 requests file.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 20:21

'''
    target：requests 高级用法，文件上传
    模拟文件上传
'''

import requests

# rb 以二进制的形式读取数据
files = {
    "file":open('favicon.ico', 'rb')
}

r = requests.post("http://httpbin.org/post", files=files)
print(r.text)