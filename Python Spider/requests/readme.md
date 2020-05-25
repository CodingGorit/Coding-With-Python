# Python 爬虫之 requests 库
学习笔记记录至：崔庆才老师的 52讲 爬虫课教程 + 网易云 5天爬虫入门课
### 1.0 requests 库快速入门
目标：学习requests 库基本用法  
安装 requests 库：  
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests  

我们平时上网的的基本流程    
1. 对一个网页（url）发起网络请求
2. 这个网络请求会先经过 DNS 服务器，找到 url 对应的 IP 地址
3. 找到这个 IP 地址之后，服务器就会针对我们的请求进行进行处理
4. 服务器处理完后，就会把响应结果给我们，比如 HTML + CSS + JS ，有时候还会有 图片，视频等二进制内容  

```Python
#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 01 requests.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/18 18:03
'''
    编写你的第一个 requests 程序
'''
# 1. 导入 requests 库
import requests
# 2. 定义请求的路径 url
url = "http://httpbin.org/get"
# 3. 发送一个 get 请求
r = requests.get(url=url)
print(r)  # 返回一个response 对象，可以看到状态码
# 4. 获取得到的内容
print(r.text) # 获取爬取到的信息
print(r.status_code) # 查看响应状态码
# 5. 获取到网页源代码之后，就是解析网页源代码，获取我们需要的信息 （数据提取）
```

该实例向我们展示了一个简单的爬虫程序，总共分为如下几步    
1. 导入 requests 库
2. 设置 url 路径（你要对哪个路径发起请求）
3. 获取响应对象 （要看是 get 还是 psot 还是 put 等等。。。）
4. 根据响应对象得到响应结果
5. 数据清洗，得到自己想要的数据 
  
### 2.1 requests response 常见响应体
该示例向我们展示了几种常见的响应结果  
1. status_code  响应状态码，通过这个我们可以很清楚判断我们的请求是否成功
• 200 请求成功
• 304 资源被重定向了
• 404 资源找不到了
• 500 服务器错误
2. headers 获取响应头
3. cookies 获取 cookies 信息
4. url 获取请求的 url 地址
5. history 获取请求历史
```Python
#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 01 requests response.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 20:09
'''
    target: 查看请求参数
'''
import requests
r = requests.get("http://static1.scrape.cuiqingcai.com/")
print(type(r.status_code), r.status_code) # 响应状态码
print(type(r.headers), r.headers) # 响应头
print(type(r.cookies), r.cookies) # 打印 cookies 信息
print(type(r.url), r.url) # 请求路径
print(type(r.history), r.history) # 请求历史
print(requests.codes.ok) # 内置状态码查询对象  ok 代表 200
```

### 2.2 requests get 常见请求之 get 请求
• 学习Python 的 get 库的请求基本使用
• 学习使用 get 请求携带参数
```Python
#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 02 requests get.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 19:47
'''
    target: 发送 get 请求，并携带参数
'''
import requests
# 不建议这样使用
url_get_params = "http://httpbin.org/get?name=geeg&age=25"
url = "http://httpbin.org/get"
data = {
    "name":"coco",
    "age":18
}
# 使用 params 实现 get 请求传参
r = requests.get(url, params=data)
print(r.text) # 直接获取网页的信息
# print(r.json())  # 如果服务器 返回的 是 json 数据，用这个方法解析
```

### 2.3 requests headers 参数
我们爬取一些网页的时候，会被网页直接拒绝请求，因为他们的服务器会检查我们的请求头是不是一个真实的游览器，如果不是游览器，我们可以在服务器返回的结果中查看到我，我们发送的其实是一个 Python requests 请求
```Python
#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 02 requests headers.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/18 18:26
'''
        target： 发送请求携带请求头
'''
import requests
# url = 'https://www.lmonkey.com/'
url = "https://www.xicidaili.com/nn" # 反爬，服务器拒绝
# 使用 headers 参数添加请求头
# 为什么要添加请求头呢？ 服务器如果验证请求头，会发现我们是 Python request，服务器会直接禁止我们的请求
headers = {
   # 这里使我们自己添加的，可以改成其他的游览器
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"
}
res = requests.get(url=url,headers=headers)
code = res.status_code # 响应状态码
print(code)
if code == 200:
    # 下载爬取的网页，写的时候会默认以 gbk 的形式写，为防止乱码，改变编码格式为 utf-8
    with open("./test.html","w",encoding="utf-8") as fp:
        fp.write(res.text)
```

### 2.4 requests post  常见请求之 post 请求
• post 请求的基本使用  
• post 请求携带参数  
```Python
#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 02 requests post.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 20:03
'''
    target：post 请求，并携带参数
'''
import requests
data = {
    "name":"coco",
    "age":25
}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
```
### 3.0 requests bin  二进制数据处理
-  使用 response.content 获取 二进制数据  
-  保存获得的二进制数据  
```Python
#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 03 requests bin.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 19:55
# 爬取二进制数据，比如图片，音乐等等二进制信息
'''
    target: 获取二进制信息，并下载下来
    这个案例是爬取 Github 的 icon，并保存到本地
'''
# 下面以爬取 github 的图标为例
import requests
r = requests.get("https://github.com/favicon.ico")
# print(r.text)  # 图片转换成字符串，打印乱码
# print(r.content) # 获取二进制信息
img = r.content
# 使用文件写入一个二进制文件
with open("favicon.ico","wb") as f:
    f.write(img)
```
### 4.1 login with cookie  使用 cookie 爬取需要登录的网站
找到一个登陆的网站，打开 F12 开发者工具，找到 request header，把 cookie 的部分全部 copy 下来，然后放进我们的请求头中，这里以为的 csdn 个人页面为例，当然并不是所有的网站都支持这么做，比如有验证码之类的呀。  
```Python
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
```
### 4.2 requests cookie  遍历 cookie 信息
我们打印 cookie 的信息  
```Python
#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 04 requests cookie.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/18 23:17
'''
    target: requests 高级用法 Cookies
'''
import requests
url = "http://www.baidu.com"
r = requests.get(url)
print(r.cookies)
# 遍历输出每一个 cookie 的键值对
for key, value in r.cookies.items():
    print(key + '=' + value)
```
### 5.0 requests session 维持会话
当我们设置 cookie ，进入了一个网页，然后想在当前会话继续进行操作发现被禁止了，这个时候就得使用 session 开启另一个会话完成剩下的爬取操作  
```Python
#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 05 requests session.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/19 0:27
'''
    使用 session 维持当前会话
    体验同一个 session 和 不同 session 操作
    使用场景，使用 cookie 登录一个网站之后，就可以使用 session 进行下一步操作
'''
import requests
s = requests.Session()
# 请求设置 cookie
requests.get("http://httpbin.org/cookies/set/number/123456789")
r = requests.get("http://httpbin.org/cookies") # 获取当前的 cookie
s.get("http://httpbin.org/cookies/set/number/123456789")
r1 = s.get("http://httpbin.org/cookies")
print("cookie："+r.text)  # 发现得不到
print("session："+r1.text) # session 可以得到
```
### 6.0 requests file  python 模拟文件上传操作  
指定我们要上传的文件即可   
```Python
#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 06 requests file.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 20:21
'''
    target：requests 高级用法，文件上传
    模拟文件上传
'''
import requests
# rb 以二进制的形式读取数据
files = {
    "file":open('favicon.ico', 'rb')
}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)
```
响应结果：这个网站可以根据我们请求的信息返回一些状态内容    
```JSON
{
  "args": {}, 
  "data": "", 
  "files": {
    "file": "data:application/octet-stream;base64,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AAAAAAAAKysrBhYWGUcWFhiVFRUYvxUVGNkWFhfzFhYX8xUVGNkVFRi/FhYYlRYWGUcrKysGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
  }, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "6665", 
    "Content-Type": "multipart/form-data; boundary=9385835bea48a3bc78a70e4bedbfd63d", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.22.0", 
    "X-Amzn-Trace-Id": "Root=1-5ecbd239-99ba03afb45871bf26673e04"
  }, 
  "json": null, 
  "origin": "这里会显示你当前的 IP 地址", 
  "url": "http://httpbin.org/post"
}
```
### 7.0 requests timeout 设置超时处理
```Python
#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 08 requests timeout.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 20:52
'''
    超时处理： timeout 参数 （防止服务器不能正常响应而抛出异常）
'''
import requests
# 设置超时时间为 1s （连接 + 读取）， 永久等待设置 timeout = None
r = requests.get("https://httpbin.org/get", timeout = 1)
print(r.status_code)
```
### 8.0 requests 完成 OuAh 认证
```Python
#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 09 requests Ouah.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 21:02
'''
    处理身份认证的情况（Outh2 身份认证）
    解决方案：使用 requests 库自带的身份认证功能，通过 auth 参数课设置
    第三方：requests_oauthlib
'''
import requests
from  requests.auth import HTTPBasicAuth
r = requests.get("https://stastic3.scrape.cuiqingcai.com/", auth=HTTPBasicAuth("admin","admin"), verify=False)
# 默认的就是 HTTPBasicAuth，可以直接使用元组代替 auth=('admin','admin')
print(r.status_code)
```
### 9.0 requests proxies 代理爬虫
```Python
#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 10 requests proxy.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 21:09
'''
    爬虫代理设置
    socks 库代理： pip3 install "requests[socks]"
'''
import requests
# 可以在网上找一些免费的代理爬虫池试一试
proxies = {
    'http':'http//10.10.10.10:1000',
    'https:':'http://10.10.10.10:1000'
}
requests.get("https://httpbin.org/get",proxies=proxies)
```
### 10 requests ssl  ssl 证书失效的网页爬取
```Python
#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 10 requests ssl.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/25 20:43
'''
    target： 爬取一些 SSL 证书配置不完整的网站
    解决方案：使用 verify 参数控制是否验证证书，否则 爬取的时候就会报 SSL 的错误
'''
import requests
from requests.packages import urllib3
import logging
# 忽略警告，但是这个方式前提是 sslError 报错解决
urllib3.disable_warnings()
# 日志记录报错信息，也可以忽略警告，前提是 sslError 报错解决
logging.captureWarnings(True)
# 方式三：使用本地证书
r = requests.get("https://static2.scrape.cuiqingcai.com/")
# print(r.status_code)
'''
    报错 OpenSSL.SSL.Error
'''
# 这个方案在 Python 3.7.1 目前是不能用的
r1 = requests.get("https://static2.scrape.cuiqingcai.com/", verify=False)
# print(r1.status_code)
```