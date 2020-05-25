#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 10 requests ssl.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 20:43

'''
    target： 爬取一些 SSL 证书配置不完整的网站
    解决方案：使用 verify 参数控制是否验证证书，否则 爬取的时候就会报 SSL 的错误
'''

import requests
from requests.packages import urllib3
import logging
# 忽略警告，但是这个方式前提是 sslError 报错解决
urllib3.disable_warnings()

# 日志记录报错信息，也可以忽略警告，前提是 sslError 报错解决
logging.captureWarnings(True)

# 方式三：使用本地证书
r = requests.get("https://static2.scrape.cuiqingcai.com/")
# print(r.status_code)
'''
    报错 OpenSSL.SSL.Error
'''

# 这个方案在 Python 3.7.1 目前是不能用的
r1 = requests.get("https://static2.scrape.cuiqingcai.com/", verify=False)
# print(r1.status_code)