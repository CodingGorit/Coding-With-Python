#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 04 login with cookie.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 20:26

'''
    target: 登录携带 cookie，我找到一个登录的网站，通过 f12 打开开发者工具，找打请求头的 cookie 部分，全部粘贴进来
    这里以我的 csdn 为例
'''

import requests

url = "https://blog.csdn.net/caidewei121"

# 这是一种传递 cookies 的方式，也是比较轻松的一种方式
headers = {
    "User-Agent": "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    "cookie": "uuid_tt_dd=10_19730278830-1590393952902-449526; dc_session_id=10_1590393952902.474841; TY_SESSION_ID=1b67bf76-0fab-4f16-8c45-66fc18dbb731; dc_sid=83482572b1ae2fcd3c1b147289695dc2; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_19730278830-1590393952902-449526!5744*1*caidewei121; __gads=ID=bf092f79b4235398:T=1590394864:S=ALNI_MbiU_uJ-dL6VwmYum9N-h78GvjrlQ; c-toolbar-writeguide=1; SESSION=c501d353-308d-480f-9e7d-252bf2cfeec4; UserName=caidewei121; UserInfo=d6365f7d4e534ba8b05ad6380dc9c7ed; UserToken=d6365f7d4e534ba8b05ad6380dc9c7ed; UserNick=Gorit; AU=4F2; UN=caidewei121; BT=1590398096436; p_uid=U100000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%7D; c_first_ref=www.baidu.com; c_utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fbss.csdn.net%252Fm%252Ftopic%252Flive_recruit%253Futm_source%253Dannounce0515%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; c_first_page=https%3A//blog.csdn.net/qq_21644175/article/details/79966397; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1590401494,1590401798,1590406388,1590407864; dc_tos=qaw03s; c_ref=https%3A//blog.csdn.net/qq_21644175/article/details/79966397; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1590409864"
}

# 另一种就是在请求的过程中，在请求头加入 cookies，这里就不方便演示了
r = requests.get(url,headers)

print(r.text)