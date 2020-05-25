#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 09 requests proxy.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 21:09

'''
    爬虫代理设置
    socks 库代理： pip3 install "requests[socks]"
'''
import requests

proxies = {
    'http':'http//10.10.10.10:1000',
    'https:':'http://10.10.10.10:1000'
}
requests.get("https://httpbin.org/get",proxies=proxies)