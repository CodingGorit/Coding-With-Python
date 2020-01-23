#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 03 login.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/20 12:44

import requests
from lxml import etree

# 封装类，进行学习猿地的登录和订单的获取
class lMonKey():
    # 登录请求地址
    loginUrl = "https://www.lmonkey.com/login"
    # 账户中心地址
    orderUrl = "https://www.lmonkey.com/my/order"

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"
    }

    # 请求对象
    req = None
    # token 口令
    token = ''
    # 订单号

    # 初始化的方法
    def __init__(self):
        # 请求对象的初始化
        self.req = requests.session()
        if self.getlogin(): # get 登录成功
            if self.postlogin(): # post 登录成功
               self.getordder()


    # get 登录页面，获取 _token
    def getlogin(self):
        # 1. get 请求 login页面，设置 cookie，获取_token
        res = self.req.get(url=self.loginUrl,headers=self.headers)
        if res.status_code == 200:
            print("get 页面请求成功")
            html = etree.HTML(res.text)
            self.token = html.xpath("//input[@name='_token']/@value")[0]
            #找到 input 标签下的，属性为 name="_token" 的标签，找它的 vcalue 的值，也就是 token 的值
            # input[@name='xxx'] 找到指定标签
            print("token 获取成功")
            return True
        else:
            print("请求错误")

    # post 登录，设置 cookie
    def postlogin(self):
        uname = input("输入你的手机号:")
        passw = input("请输入你的密码:")

        data = {
            "_token": self.token,
            "username": uname,
            "password": passw
        }
        # 发起 post 请求
        res = self.req.post(url=self.loginUrl,headers=self.headers,data=data)
        if res.status_code==200 or res.status_code==302:
            print("登录成功！！")
            return True

    def getordder(self):
        # 获取订单页，使用 get 请求即可，获取默认订单号
        # 解析数据即可
        res = self.req.get(url=self.orderUrl,headers=self.headers)
        if res.status_code == 200:
            print("请求订单页页面成功")
            html = etree.HTML(res.text)
            # 頁面解析
            r = html.xpath("//div[@class='avatar-content']/small/text()")
            print(r)
        else:
            print("頁面請求失敗")

obj = lMonKey()
