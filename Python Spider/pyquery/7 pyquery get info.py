#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 7 pyquery get info.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/29 20:17

'''
    获取信息
        1. 获取属性
        2. 获取文本
'''

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
# 通过 dom 得到 a标签
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href')) # attr 方法中传入 属性即可得到值了
print(a.attr.href) # 通过 属性.参数 一样可以得到数据

a1 = doc('li a')
for item in a1.items():
    print(item.attr('href'))

print("===============")
# 获取文本 通过 text 方法实现
li = doc('li')
print(li.html()) # 只能获得一个节点
print("===============")
print(li.text()) # 可以获得所有的 节点的内容，并使用字符串拼在一起
print("===============")
for lis in li.items():
    print(lis.html())
    print(lis.text())