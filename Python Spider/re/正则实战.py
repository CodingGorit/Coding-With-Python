# -*- coding: utf-8 -*-
#file: 实战.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/23 16:41


'''
数据地址：https://www.lmonkey.com/ask
数据字段：问题，时间，作者
'''
import requests,re,io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# 1 定义请求的 url 和 请求头
url = "https://www.lmonkey.com/ask"
headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 7.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"
}

# 2. 发起请求
res = requests.get(url=url,headers=headers)

# 3 检测请求是否成功
if res.status_code == 200:
    # 4. 获取返回的数据
    res_html = res.text

    # 5 数据的解析
    reg = '<div class="topic_title mb-0 lh-180 ml-n2">(.*?)<small'
    reg1 = '<span data-toggle="tooltip" data-placement="top" title="(.*?)">'
    reg2 = "<strong>(.*?)</strong>"

    # 调用正则的方法获取问题的标题
    titlelist = re.findall(reg,res_html)
    authorlist = re.findall(reg2,res_html)
    pubdatelist = re.findall(reg1,res_html)
    authorurllist = re.findall('<a href="(https://www.lmonkey.com/ask/\d+)" target="_blank">',res_html)
    print(authorurllist,len(authorurllist))