#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 3 pyquery file.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/26 22:26

'''
    pyquery 读取 html文件
'''

from pyquery import PyQuery as pq
doc = pq(filename='test.html')
print(doc('li'))

'''
    必须保证本地有 HTML 文档
    1. 它会先读取本地文件的内容
    2. 然后将这个字符串传递给 pyquery 初始化
'''