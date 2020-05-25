#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 05 requests session.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/19 0:27

'''
    使用 session 维持当前会话
    体验同一个 session 和 不同 session 操作
    使用场景，使用 cookie 登录一个网站之后，就可以使用 session 进行下一步操作
'''

import requests

s = requests.Session()
# 请求设置 cookie
requests.get("http://httpbin.org/cookies/set/number/123456789")
r = requests.get("http://httpbin.org/cookies") # 获取当前的 cookie


s.get("http://httpbin.org/cookies/set/number/123456789")
r1 = s.get("http://httpbin.org/cookies")

print("cookie："+r.text)  # 发现得不到
print("session："+r1.text) # session 可以得到