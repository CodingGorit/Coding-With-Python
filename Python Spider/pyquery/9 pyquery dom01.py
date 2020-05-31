#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 9 pyquery dom01.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/29 20:48

'''
    attr： 对属性操作
    text： 修改节点的内容
    html：
'''

html = '''
<ul class="list">
     <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name', 'link') # 修改属性
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>') # 插入 html
print(li)

