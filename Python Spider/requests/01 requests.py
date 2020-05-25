#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 01 requests.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/18 18:03

'''
    编写你的第一个 requests 程序
'''
# 1. 导入 requests 库
import requests

# 2. 定义请求的路径 url
url = "http://httpbin.org/get"

# 3. 发送一个 get 请求
r = requests.get(url=url)

print(r)  # 返回一个response 对象，可以看到状态码

# 4. 获取得到的内容
print(r.text) # 获取爬取到的信息
print(r.status_code) # 查看响应状态码

# 5. 获取到网页源代码之后，就是解析网页源代码，获取我们需要的信息 （数据提取）