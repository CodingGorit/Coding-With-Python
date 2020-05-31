#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 1 pyquery start.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/26 21:59

'''
    pyquery 快速入门
'''

from pyquery import PyQuery as pq

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

doc = pq(html)
print(doc)   # 打印 html
print(doc('li'))  # 获取所有的 li 标签

'''
总结：
    1. 首先引入 pyquery 库，并使用别名 pq
    2. 然后声明一个较长的 HTML 字符串，作为当前的参数，传入 pyquery类（初始化完成）
    3. 然后获取所有的 li 节点
'''