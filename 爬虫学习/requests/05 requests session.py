#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 05 requests session.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/19 0:27
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"
    # 在 headers 里面手动添加 cookie，笨方法
}

data = {
    "csrftoken": "1e12e363-1755-48ab-baa2-b5da5ff69e38,1e12e363175548abbaa2b5da5ff69e38",
    "yhm": "20171111034",
    "mm": "VgRpzwymHpDomMSci1UYa1oM/MBEwiGsHQdKvYCkm7d7Fk+Rkl+7Sy7laEaZlGZ2mvOQFwdvNq69U1nn4QRM0pet8lADshzaYEfAnt28gNlVOf1qvMfS93V7TL9CFNdxqDqSjuMfMWXRF8dU4AKDt6GG1n3fKYTYwGJxwhMTRW0=",
    "mm": "VgRpzwymHpDomMSci1UYa1oM/MBEwiGsHQdKvYCkm7d7Fk+Rkl+7Sy7laEaZlGZ2mvOQFwdvNq69U1nn4QRM0pet8lADshzaYEfAnt28gNlVOf1qvMfS93V7TL9CFNdxqDqSjuMfMWXRF8dU4AKDt6GG1n3fKYTYwGJxwhMTRW0="
}

url = "http://syjw.wsyu.edu.cn/xtgl/login_slogin.html"
loginurl ="http://syjw.wsyu.edu.cn/bysxxcx/xscjzbdy_cxXscjzbdyIndex.html?gnmkdm=N558020&layout=default&su=20171111034"
req = requests.session()

res = req.post(url=loginurl,headers=headers,data=data)

code = res.status_code
print(code)
if code == 200:
    with open("./rr.html","w",encoding="utf-8") as fp: # 写的时候会默认以 gbk 的形式写
        fp.write(res.text)