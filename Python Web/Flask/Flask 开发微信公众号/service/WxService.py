#!/usr/bin/python
# -*- coding: utf-8 --
#@File: WxService.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/3/4 0:13
import time

import requests,json
__APPID = "wx1c1862f2b751664f"
__APPSECRET = "79c893f62a9a35f9ca427b7d8fbbe4da"
__GET_ACCESS_TOKEN = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={__APPID}&secret={__APPSECRET}"
getUserListUrl = f"https://api.weixin.qq.com/cgi-bin/user/get?access_token=TOKEN"
template_id = "yFGAYVyatZSiXD9asBEfiXg0ULLbo-7rV9fHVD5rSQ4"
setIndustryUrl = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=ACCESS_TOKEN"

# 获取 token
def getToken():
    res = requests.get(__GET_ACCESS_TOKEN)
    if res.status_code == 200:
        access_token = res.json()
        Token = access_token["access_token"]
        # expires_in = res.text["expires_in"]
        return Token

def get_user_list():
    url = getUserListUrl.replace("TOKEN",getToken())
    res = requests.get(url)
    if res.status_code == 200:
        print("请求成功")
        print(res.text)
    else:
        print("请求失败")

def send_event(openID):
    url = setIndustryUrl.replace("ACCESS_TOKEN",getToken())
    now = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime (time.time ()))
    data = {
        "touser": openID,

        "template_id": "Oyvz7NlnNvhdypIAfwCfC8B_pJXJI1kJcB_W2Fk09Ls",
        # 接收消息跳转的链接
        "url": "http://weixin.qq.com/download",

        "topcolor": "#FF0000",

        "data": {

            "User": {

                "value": "同学",

                "color": "#173177"

            },

            "Date": {

                "value": now,

                "color": "#173177"

            },

            # "Next": {
            #     "value": "下节课是微积分 A1",
            #     "color": '#333'
            # },

            "Test" : {
                "value": "上课了，上课了",
                "color": "#000"
            },

            "remark" : {
                "value": "好好听讲，请不要逃课哦",
                "color": "#999999"
            }

        }

    }
    res = requests.post(url,data=json.dumps(data))
    if res.status_code == 200:
        print(res.json())
    else:
        print("請求失敗")

if __name__ == '__main__':
    # get_user_list()
    send_event()