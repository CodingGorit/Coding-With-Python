#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 4 pyquery css selector.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/26 22:35

'''
    pyquery css 选择器
'''

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
# 和 css 的 id 选择器， class 选择器一样
print(doc('#container .list li'))

# 循环遍历并节点内容
list = doc('#container .list li').items()
for item in list:
    print(item.text()) # 遍历并获取节点内容
