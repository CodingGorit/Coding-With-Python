#!/usr/bin/python
# -*- coding: utf-8 --
#@File: CheckUtil.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/3/3 23:46
import hashlib


def Check_Url(request):
    # 表示是第一次接入微信服务器的验证
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    token = "imooc"
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1 ()
    sha1.update (list[0].encode ('utf-8'))
    sha1.update (list[1].encode ('utf-8'))
    sha1.update (list[2].encode ('utf-8'))
    hashcode = sha1.hexdigest ()
    echostr = request.args.get ("echostr")
    if hashcode == signature:
        return signature
    else:
        return signature