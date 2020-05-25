#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: requests post.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/18 19:53

'''
    模拟百度翻译
'''

import requests

def get_url_content(url,data):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"
    }
    res = requests.post (url=url, data=data,headers=headers, timeout=3000)
    return res

def get_user_kw():
    data = dict()
    x = input("请输入你要查询的语句:")
    data["kw"] = x
    return data

def data_process(res):
    if res.status_code == 200:
        print(res.json())
        ans = res.json()
        if ans["errno"] == 0: # 错误码为0，结果正常请求得到
            v = ans["data"][0]
            # print(v)
            k = v['v']
            result = k.split(";")
            return result[-2].strip(" ")

if __name__ == '__main__':
    url = "https://fanyi.baidu.com/sug"
    data = get_user_kw() # 获取用户输入的值
    res = get_url_content(url=url,data=data) # 获取网页的内容
    result = data_process(res=res)
    print(result)