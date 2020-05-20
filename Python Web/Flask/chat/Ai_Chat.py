#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: Ai_Chat.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/2/26 22:52

from flask import Flask, url_for, render_template,request
from flask import request
from Flask.chat.api import robot
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
'''
    1. 首先加载 html 文件
    2. 接收 html 文件发送过来的请求，就是用户输入的内容
    3. 服务器处理之后，返回指定的数据回去
    4. 将返回的数据显示到页面上
'''

@app.route("/")
def req():
    return render_template('chat.html')

# 解决跨域问题

@app.route('/api/res',methods = ['GET','POST'])
def get_res():
    query = request.args.get('query')
    print(query)
    if query is None:
        return "抱歉，请刷新再试试"
    return robot.get_content (query)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=80,debug=True)