#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 6 pyquery foreach.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/27 0:03

'''
    遍历
    pyquery 的选择结果可能是多个节点，也有可能是单个节点
'''
from pyquery import PyQuery as pq
doc = pq(filename="test.html")

# 通过 items 获得每一项, 得到一个生成器
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li.text(), type(li))