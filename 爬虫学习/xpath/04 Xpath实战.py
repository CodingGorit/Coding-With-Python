#!/usr/bin/python
# -*- coding: utf-8 -*-
# file: 04 Xpath实战.py
# @author: Gorit
# @contact: gorit@qq.com
# @time: 2020/1/20 14:32
import requests
from lxml import etree

url = "https://www.lmonkey.com/toutiao"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
}
# response = requests.get(url=url,headers=headers)

# 解析一个 html文件
html = etree.parse ("./yq.html", etree.HTMLParser ())

# etree.HTML(text) 读取网页原内容
titles = html.xpath ("//div[@class='topic_title mb-0  essence_title yh']/text()")
authors = html.xpath ("//div[contains(@class,'list-group-item list-group-item-action')]/strong/a/text()")
url = html.xpath ("/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div/div[2]/a[1]/@href")

print (url)
