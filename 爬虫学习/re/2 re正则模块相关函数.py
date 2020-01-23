#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 2 re正则模块相关函数.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/22 22:09

import re
# re 正则相关函数
'''
re.match()
    + 从头开始匹配
    + 要么第一个字符符合要求，要么不符合，返回 None
    + 匹配成功，返回 Match 对象，否则返回 None
    + 可以使用 group() 获取返回对象
    + 可以使用 span() 获取匹配的数据的下标区间
re.search()
    + 从字符串开头到结尾开始搜索匹配
    + 匹配成功，返回 Match 对象，否则返回 None
    + 可以使用 group() 获取返回对象
    + 可以使用 span() 获取匹配的数据的下标区间
search() 和 match()  方法的区别
    match() 是从字符串的开头进行匹配，如果开始就不符合匹配请求，就返回 None
    search() 方法是从字符串开始位置一直搜索到最后，如果整个字符串中都没有搜索到，则返回 None
    

'''

vars = "iloveyou521tosimida"

reg = "love" #

# search()
res = re.search(reg,vars)
print(res)
print(res.group())
print(res.span())

# 调用 match 函数
# reg = "ilove" 才会有反应
# res = re.match(reg,vars) # reg = "love" 返回 None
# print(res) # 打印的是对象
# print(res.group()) # 获取返回字符串的数据结果
# print(res.span()) # 返回字符串匹配结果的下标区间

