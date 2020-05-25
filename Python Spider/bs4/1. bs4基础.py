#!/usr/bin/python
# -*- coding: utf-8 -*-
# file: 1. bs4基础.py
# @author: Gorit
# @contact: gorit@qq.com
# @time: 2020/1/20 15:02

from bs4 import BeautifulSoup

text = '''
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>我的第一个网页</title>
</head>
<body>
    <ul>
        <li><a href="/a/b/c/java" id="link1">java 工程师</a></li>
        <li><a href="/a/b/c/python" id="link2">Python 工程师</a></li>
        <li><a href="/a/b/c/C" id="link3">C++ 工程师</a></li>
    </ul>
    <p class="title">Hello World</p>
    <p class="ttt" id="link">aaba</p>
    <p class="aaa">aaaa</p>
</body>
</html>
'''

soup = BeautifulSoup (text, "lxml")  # 使用 lxml 解析

# 获取指定元素，或者元素的属性值 ，要么获取文本
# r = soup.title["abc"]
# r = soup.title
# r = soup.p
# r = soup.p['class'] # 获取元素的 class 属性
# r = soup.p.b # 获取元素 p 下的 b 元素
# r = soup.title.text # 获取标签的文本
# r = soup.p.parent.name # 获取父级元素的名字  body
# r = soup.p.text # 查找 p 标签之间的内容
# print(r)

# 搜索获取页面元素中的元素  find  find_all
# r = soup.findAll("a") # 找到所有的 a标签, find 获取第一个
# r = soup.find(class_="2") # 找到 class 为 '2' 的元素
# r = soup.find(id = "link") # 找指定 id 的标签， r.text 获取标签之间元素
# print(r.text) # 获取标签之间的值
# print(r.get_text()) # 获取标签之间的值

# css 选择器

# 通过标签 选择元素
# r = soup.select("title")
# print(r)

# 通过 class类名选取元素
# r = soup.select(".title") # 使用 css 选择器选择元素
# print(r)

# 通过 ID 选择元素
# r = soup.select("#link1")
# print(r)

# 通过 空格，层级关系获取元素
# r = soup.select("html body p")
# r = soup.select("html body a")
# print(r)

# 通过 逗号，并列关系获取元素
# r = soup.select("a,title")
# print(r)

# 其他搜索
# find_parents() 返回祖先节点
# find_parent()
r = soup.f
