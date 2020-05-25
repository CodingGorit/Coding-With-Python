#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 08 requests Ouah.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 21:02

'''
    处理身份认证的情况（Outh2 身份认证）
    解决方案：使用 requests 库自带的身份认证功能，通过 auth 参数课设置
    第三方：requests_oauthlib
'''
import requests
from  requests.auth import HTTPBasicAuth

r = requests.get("https://stastic3.scrape.cuiqingcai.com/", auth=HTTPBasicAuth("admin","admin"), verify=False)
# 默认的就是 HTTPBasicAuth，可以直接使用元组代替 auth=('admin','admin')
print(r.status_code)