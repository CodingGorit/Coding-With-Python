#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 04 request 之携带 cookie.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/18 23:17

import requests
url = ""

headers = {
    "User-Agent": "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"
    # 在 headers 里面手动添加 cookie，笨方法
}


res = requests.get(url=url)