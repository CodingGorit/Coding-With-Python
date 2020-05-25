#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 豆瓣电影 top250.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/26 16:21

'''
数据爬取，然后存进 json 中

'''

import time
import requests
from lxml import etree
import sys,io
import json

def getPages(url):
    ''' 请求页面数据'''
    try:
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"
        }
        # 发起请求
        res = requests.get(url,headers=headers)
        # 判断响应状态
        if res.status_code == 200:
            return res.text.encode("utf-8")
        else:
            return None
    except:
        return None


def parsePage(html):
    ''' 解析页面数据'''
    html = etree.HTML(html)
    items = html.xpath("//div[@class='item']")
    # 遍历封装数据并返回
    for item in items:
        res = {
            'index':item.xpath(".//div/em[@class='']/text()"),
            'image':item.xpath(".//img[@width='100']/@src"),
            'title':item.xpath(".//span[@class='title']/text()"),
            'actor':item.xpath(".//p[@class='']/text()"),
            'score':item.xpath(".//span[@class='rating_num']/text()")
        }
        print(res)
        yield res

def writeFile(item):
    ''' 写入数据'''
    with open("./豆瓣.json",'a',encoding="utf-8") as f:
        f.write(json.dumps(item))
        f.write("\n")

def main(offset):
    ''' 主程序函数，负责爬虫程序 '''
    url = f"https://movie.douban.com/top250?start={offset}"
    # 调用函数进行页面的爬取
    html = getPages(url)
    if html:
        print(f"正在解析 url:{url}")
        # 解析页面数据 parsePage(html)
        for item in parsePage(html):
            print(f"正在写入数据{item['title']}")
        # 写入数据 writeFile(item)
            writeFile(item)

if __name__ == '__main__':
    # main(0)
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    for i in range(0,10):
        main(i*25)
        time.sleep(2)