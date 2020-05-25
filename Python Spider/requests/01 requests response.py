#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 01 requests response.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 20:09

'''
    target: 查看请求参数
'''

import requests

r = requests.get("http://static1.scrape.cuiqingcai.com/")
print(type(r.status_code), r.status_code) # 响应状态码
print(type(r.headers), r.headers) # 响应头
print(type(r.cookies), r.cookies) # 打印 cookies 信息
print(type(r.url), r.url) # 请求路径
print(type(r.history), r.history) # 请求历史
print(requests.codes.ok) # 内置状态码查询对象  ok 代表 200