#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 有道翻译.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/23 17:41

import requests
def get_result(keywords):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {
        'i': keywords,
        "doctype": "json"
    }
    res = requests.post (url=url, data=data)
    code = res.status_code
    if code == 200:
        # print(res.json())
        errcode = res.json ()['errorCode']
        if errcode == 0:
            res_data = res.json ()['translateResult'][0][0]['tgt']
            return res_data
    else:
        print("翻译失败")
if __name__ == '__main__':
    vars = '''
    xxxxxxxxxxxxxxxxxx
    xx欢迎来到 Py 翻译xx
    xx  输入 q 退出  xx
    xxxxxxxxxxxxxxxxxx
    '''
    print(vars)
    while True:
        key_word = input("请输入你要翻译的语句:")
        if key_word == 'q':
            break
        res = get_result(key_word)
        print(res)



