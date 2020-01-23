#!/usr/bin/python
# -*- coding: utf-8 -*-
# file: 爬取指定网页.py
# @author: Gorit
# @contact: gorit@qq.com
# @time: 2020/1/22 20:52

# 爬取 学习源地

import requests,json
from bs4 import BeautifulSoup

# 定义请求的 url 和 请求头
url = "https://www.lmonkey.com/t"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 7.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"
}

# 发送请求
res = requests.get(url=url,headers=headers)
if res.status_code == 200:
# 解析数据
    soup = BeautifulSoup(res.text,"lxml")
    divs = soup.find_all("div",class_="list-group-item list-group-item-action p-06")
    varlist = []
    for i in divs:
        r = i.find("div",class_="topic_title")
        if r:
            print()
            vardict = {
                    "title":r.text.split("\n")[0],
                    "url":i.a["href"],
                    "author":i.strong.a.text,
                    "publishdate":i.span["title"]
            }
            varlist.append(vardict)
    print(varlist)
    # 写入数据
    with open("./yq.txt","w",encoding="utf-8") as f:
        f.write(str(varlist))


