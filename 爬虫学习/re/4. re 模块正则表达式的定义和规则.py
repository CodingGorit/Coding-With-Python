#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 4. re 模块正则表达式的定义和规则.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/22 22:54

import re
# 正则表达式规则定义

# 普通字符 字符串，+
# vars = "iloveu"
#
# reg = 'love'
# res = re.search(reg,vars).group()
#
# print(res)

# 转义字符 \w \W \d \D \s \S ....
# \d 代表单个数字
# \D 代表单个非数字
# \w 代表单个字母，单个数字，下划线
# \W 代表单个非字母，下划线。。
# \s 代表单个空格符、或制表符
# \S 代表的单个非空格，非制表符
# 匹配多串内容，组合使用  reg = '\w\w\w\w\d'
# varstr = "$_ilove521you"
#
# reg = '\w\w\w\w\d'
#
# res = re.search(reg,varstr).group()
# print(res,len(res))

# 特殊字符 . * + ? {} [] () ^ $
# . 代表单个的任意字符，除了换行符之外
# .*，\w* 代表匹配次数，代表任意次数
'''
 如果使用 *号，那么在匹配开始处如果符合要求，
 那按照规则一直向后匹配，直到不符合匹配规则结束并返回

 如果在匹配开始处不符合要求，则返回 0 次
'''
# \w+ +号 要求至少匹配一次

varstr = "hello WORLD iloveu5211imissyou"
reg = '\w+?' # 拒绝贪婪，前面的匹配规则只要达成要求就返回
reg = '\w*?' # * 代表任意次，上面 +号至少匹配一个，这里第一个都符合要求，就返回
reg = '\w{6}' # 连续匹配四个字符串 {} 代表匹配次数，1个数字表示必须匹配的次数
reg = '\w{2,5}' # 两个数字时，必须匹配的区间次数
reg = '[A-Z,a-z,0-9]' # [] 代表字符的范围  [A-Z,a-z,0-9] = \w
reg = '\w+(\d{4})(\w+)' #() 代表子组，代表整个表达式首先作为正则的一部分，另外会把括号中的内容单独领出来

varstr = '13233442211'
# 定义一个匹配手机号的正则表达式
reg = '^1\d{10}' # ^ 代表开头， $ 代表结尾


# 定义一个正则表达式，来邮箱是否正确
# 完善手机号的正则表达式
# 定义一个匹配 IP 的正则表达式

# res = re.search(reg,varstr)
# print(res.group())
# print(res.groups())

# 正则模式 re.I 不区分大小写,看官方文档
vars = 'iLOVEu'

reg = '[a-z]+'

res = re.search(reg,vars,re.I)
print(res.group())
