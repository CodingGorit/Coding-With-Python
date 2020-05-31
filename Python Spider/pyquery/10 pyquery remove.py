#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 10 pyquery remove.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/29 23:33

'''
    提取 Hello World
'''

html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
wrap = doc.find('p').remove() # 删除 dom 节点
print(doc.text())
