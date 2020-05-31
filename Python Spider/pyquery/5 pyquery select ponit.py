#!/usr/bin/python
# -*- coding: utf-8 --
#@File: 5 pyquery select ponit.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/5/26 23:30

'''
    查找节点
    常见节点查询
    1. 子节点查询
    2. 父节点查询
'''

from pyquery import PyQuery as pq
doc = pq(filename='test.html')
items = doc('.list') #查找 class 为 list 的节点内容
print(items)

# 查找子节点使用
lis = items.find('li')
print(lis)


lis1 = items.children()
print(lis1)

# 筛选出子节点中合适的节点
lis2 = items.children('.active')
print(lis2)

'''
    总结：
    1. 通过 .list 参数选取 class 为 list 的节点
    2. 然后调用 find 方法，传入 CSS 选择器，选取内部的 li 节点
    find 查找的范围是节点的所有子节点
    3. 查询子节点使用 children 方法
'''

# 获取父节点
container = items.parent()
print(container) # 得到直接父节点， container 包含的节点内容

# 获取所有祖先节点
wrap = items.parents()
print(wrap)  # 可以看到两条记录，说明会返回所有的祖先节点

# 筛选祖先节点
parent = items.parents('.wrap')
print(parent)

# 获取兄弟节点
li = doc('.list .item-0.active')
print(li.siblings())

# 筛选兄弟节点，传入 css 选择器
li1 = doc('.list .item-0.active')
print(li.siblings('.item-1.active'))

'''
    获取父节点、祖先节点，兄弟节点的方式
'''