#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 2. pyquery init url.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/26 22:05

'''
    url 初始化之使用 网页的 URL
    这里获取我的
'''

from pyquery import PyQuery as pq

# 方式一：获取我的个人网站的标题，为了防止乱码，指定编码格式
doc = pq(url='https://www.gorit.cn',encoding='utf-8')
title = doc('title')
print(title)

# 方式二：
import requests
doc1 = pq(requests.get("https://www.gorit.cn").text.encode("utf-8"))
print(doc1('title'))