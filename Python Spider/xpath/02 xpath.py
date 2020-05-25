#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 02 xpath.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/20 11:12

from lxml import etree

# 解析一个 html 文件  etree.HTMLParser() 解析文件
html = etree.parse("./test.html",etree.HTMLParser())
print(html)

# 解析
# r = html.xpath('/html/body/ul/li/a/text()')
r1 = html.xpath('//li/a/text()') # 两个斜杠直接查找,获取所有 liv 里面的元素
print(r1)

# 获取指定标签里面的元素
r2 =html.xpath("//div[@class='teacher']//li/a/text()")
print(r2)

r3 = html.xpath("//div[@class='teacher']//li/a/@href")
print(r3)

# 使用 zip 函数将链接和内容一一对应
print(list(zip(r3,r2)))

#
'''
/ 当前元素的直接子节点
// 当前元素的子节点或孙子节点

text() 获取 HTML 中的文本内容

@ 属性获取  eg 
1. @href 得到链接 
2. @value 得到值

获取第一个   li[1]
获取最后一个 li[last()]
获取前两个 li[position()<3]
获取倒数第三个 li[last()-2]
'''