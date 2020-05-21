#!/usr/bin/python
# -*- coding: utf-8 --
#@File: MessageUtil.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/3/4 13:20

import time
import xmltodict
from msg import chat

MESSAGE_TEXT = "text"
MESSAGE_IMAGE = "image"
MESSAGE_VOICE = "voice"

def res_data(data):
    # 表示微信服务器转发消息过来
    xml_str = data
    if not xml_str:
        return ""
    # 对xml字符串进行解析
    xml_dict = xmltodict.parse(xml_str)
    xml_dict = xml_dict.get("xml")

    msg_type = xml_dict.get("MsgType") # 提取消息类型
    if msg_type == MESSAGE_TEXT:
        resp_xml_str = dealTextMessage(msg_type,xml_dict)
        return resp_xml_str
    else:
        dealOtherMessage(msg_type,xml_dict)


# 处理文本消息
def dealTextMessage(MsgType,xml_dict):
    # 表示发送的是文本消息
    # 构造返回值，经由微信服务器回复给用户的消息内容
    response = xml_dict.get("Content")
    content = ''
    if response == "彩蛋":
        content = "啦啦啦"
    else:
        content = chat.get_content(response)
    resp_dict = {
        "xml": {
            "ToUserName": xml_dict.get ("FromUserName"),
            "FromUserName": xml_dict.get ("ToUserName"),
            "CreateTime": int (time.time()),
            "MsgType": MsgType,
            "Content": "巴啦啦小魔仙说:" + content
        }
    }
    # 将字典转换为xml字符串
    resp_xml_str = xmltodict.unparse (resp_dict)
    # 返回消息数据给微信服务器
    print (resp_xml_str)
    return resp_xml_str


def dealOtherMessage(MsgType, xml_dict):
    resp_dict = {
        "xml": {
            "ToUserName": xml_dict.get ("FromUserName"),
            "FromUserName": xml_dict.get ("ToUserName"),
            "CreateTime": int (time.time ()),
            "MsgType": MsgType,
            "Content": "Hello World"
        }
    }
    resp_xml_str = xmltodict.unparse (resp_dict)
    # 返回消息数据给微信服务器
    return resp_xml_str
