#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 有道翻译.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/23 17:41

import requests

s = input("请输入你要翻译的语句:")

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

data = {
    'i':s,
    "doctype": "json"
}

res = requests.post(url=url,data=data)

code = res.status_code
if code == 200:
    # print(res.json())
    errcode = res.json()['errorCode']
    if errcode == 0:
        res_data = res.json()['translateResult'][0][0]['tgt']
        print(res_data)
