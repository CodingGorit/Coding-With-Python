#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 03 requests bin.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 19:55

# 爬取二进制数据，比如图片，音乐等等二进制信息
'''
    target: 获取二进制信息，并下载下来
    这个案例是爬取 Github 的 icon，并保存到本地
'''
# 下面以爬取 github 的图标为例
import requests

r = requests.get("https://github.com/favicon.ico")
# print(r.text)  # 图片转换成字符串，打印乱码
# print(r.content) # 获取二进制信息

img = r.content

# 使用文件写入一个二进制文件
with open("favicon.ico","wb") as f:
    f.write(img)