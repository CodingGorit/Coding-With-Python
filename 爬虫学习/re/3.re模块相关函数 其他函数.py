#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 3 re模块相关函数 其他函数.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/22 22:33
import re

'''
re.findall()
    + 按照正式表达式的规则在字符串中匹配元素，结果返回一个列表，如果没有找到返回空列表
    
re.finditer()
    + 按照正则表达式的规则，在字符串中匹配所有符合规则的元素，返回一个迭代器
    （迭代器可以通过 next() 获取，for 循环遍历，list）

re.sub() 搜索替换
    + 按照正则表达式的规则，在字符串中找到需要被替换的字符串，完成一个替换
参数：
    pattern：正则表达式的规则，匹配需要被替换的字符串
    repl：替换后的字符串
    string: 被替换的原始字符

re.complie() 
    # 可以直接将正则表达式定义为 正则对象，使用正则对象直接操作
'''
# 定义字符串
vastr = 'iloveyou521tosimida511'

# 正則表達式
# reg = '\d'

# reg = '\d{3}' # {3} 表示查找连续的三个数字
# res = re.findall(reg,vastr) # 每個數字當成匹配單元
# res = re.finditer(reg,vastr) # list(res)
# res = re.sub(reg,'AAA',vastr)  # iloveyouAAtosimidaAA

# 我们自己定义正则表达式对象
# reg = re.compile('\d{3}')
# 直接使用正则对象，去掉哟红对应的方法或函数
# res = reg.findall(string=vastr)

line = {
        "i love 512 you",
        "i love 521 you",
        "i love 345 you",
        "i love 543 you"
        }

# 先预编译
reg = re.compile('\d{3}')
for i in line:
    # reg = '\d{3}'
    res = reg.search(i).group()
    print(res)

# print(res)