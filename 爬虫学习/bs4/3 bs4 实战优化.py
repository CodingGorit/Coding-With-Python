#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 3 bs4 实战优化.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/22 21:45

import requests,json
from bs4 import BeautifulSoup

# 封装类
class Bs4Yq():
    # 定义属性
    url = "https://www.lmonkey.com/t"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 7.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"
    }

    # 响应源代码的存放位置
    res_html = None
    #存储解析后的数据
    varlist = None
    # 初始化方法
    def __init__(self):
        # 发起一个请求
        res = requests.get(url=self.url,headers=self.headers)
        if res.status_code == 200:
            print("请求成功")
            self.res_html = res.text
            if self.paresData():
                self.WriteJson()
                print("数据写入成功！！！")
        else:
            print("请求失败")
            return False

        # 解析 html 数据

    def paresData(self):
        # 解析数据
        soup = BeautifulSoup(self.res_html, "lxml")
        try:
            divs = soup.find_all ("div", class_="list-group-item list-group-item-action p-06")
            varlist = []
            for i in divs:
                r = i.find ("div", class_="topic_title")
                if r:
                    print ()
                    vardict = {
                        "title": r.text.split ("\n")[0],
                        "url": i.a["href"],
                        "author": i.strong.a.text,
                        "publishdate": i.span["title"]
                    }
                    varlist.append (vardict)
            return True
        except:
            return False

    def WriteJson(self):
        if self.varlist != []:
            try:
                with open ("./yq.json", "w", encoding="utf-8") as f:
                    json.dump(self.varlist,f)
                return True
            except:
                return False
        else:
            print("无法获取当前解析的数据")
            return False

res = Bs4Yq()

