#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 豆瓣电影 top 250.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/24 16:36
# 豆瓣top250
import requests
from lxml import etree
import sys,io
import csv

def res_html(n):
    url = f"https://movie.douban.com/top250?start={25*n}&filter=" # n 的范围在 1 ~ 10
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"
    }
    res = requests.get(url=url, headers=headers)
    return res

def get_res(res):
    if res.status_code == 200:
        print("网页请求成功")
        # print(res.content.decode(encoding="utf-8"))
        res_html = etree.HTML (res.content.decode ("utf-8"))
        movie_title = res_html.xpath ('//div[@class="hd"]/a/span[1]/text()')
        movie_url = res_html.xpath ('//div[@class="hd"]/a/@href')
        movie_rating = res_html.xpath ("//span[@class='rating_num']/text()")
        return list(zip(movie_title,movie_url,movie_rating))

    # with open("./豆瓣电影评分 top250.csv","w",encoding="utf-8") as f:
    #     f.seek(1)
    #     for i in range(len(movie_rating)):
    #         f.writelines(movie_title[i]+','+movie_url[i]+','+movie_rating[i]+"\n")

    # print(movie_title)
    # print(len(movie_title))
    #
    # print(movie_url)
    # print(len(movie_url))

    # print(rating)
    # print(len(rating))

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper (sys.stdout.buffer, encoding='gb18030')
    for i in range(0,11):
        res = res_html(i)
        data = get_res(res)
        print(data)
