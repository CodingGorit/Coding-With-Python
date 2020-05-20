#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: manage.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/2/26 22:51

from flask import Flask,request
from util.MessageUtil import res_data
from util import CheckUtil

app = Flask(__name__)

@app.route('/wx', methods=["GET", "POST"])
def getinput():
    if (request.method == "GET"):
        CheckUtil.Check_Url(request)
    elif request.method == "POST":
        return res_data(request.data)

@app.route("/")
def index():
    return "Hello， 服务已经开启"

if __name__ == '__main__':
    app.run(port='80',debug=True)