#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 01 xpath.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/19 17:39

from lxml import etree

text = '''
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>我的第一个网页</title>
</head>
<body>
    <ul>
        <li><a href="/a/b/c/java">java 工程师</a></li>
        <li><a href="/a/b/c/python">Python 工程师</a></li>
        <li><a href="/a/b/c/C">C++ 工程师</a></li>
    </ul>
</body>
</html>
'''

html = etree.HTML(text)
# print(html)

# xpath 获取内容
res = html.xpath("/html/body/ul/li/a/text()")
# print(res)

r = html.xpath("/html/body/ul/li/a[1]/text()")
print(r[0])