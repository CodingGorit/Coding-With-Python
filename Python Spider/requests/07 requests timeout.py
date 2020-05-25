#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 07 requests timeout.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 20:52

'''
    超时处理： timeout 参数 （防止服务器不能正常响应而抛出异常）
'''

import requests

# 设置超时时间为 1s （连接 + 读取）， 永久等待设置 timeout = None
r = requests.get("https://httpbin.org/get", timeout = 1)
print(r.status_code)