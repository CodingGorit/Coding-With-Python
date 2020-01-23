#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 02 requests 的请求头.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/18 18:26

import requests

# url = 'https://www.lmonkey.com/'

url = "https://www.xicidaili.com/nn" # 反爬，服务器拒绝

# 添加请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"
}
res = requests.get(url=url,headers=headers)

code = res.status_code # 响应状态码
print(code)

if code == 200:
    with open("./test.html","w",encoding="utf-8") as fp: # 写的时候会默认以 gbk 的形式写
        fp.write(res.text)

# print(res.status_code)