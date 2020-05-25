#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 1 re模块.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/22 21:58

import re

# 特殊的语法规则，完成字符串的搜索，匹配等问题
'''
正则表达式组成
    普通字符：大小写字母，数字，符合
    转义字符：\w \W \d \D \s \S ..
    特殊字符 . ? * $ ……  [] {} ()
    匹配模式 I U
'''
# 定义字符串
vars = 'iloveyo521utoismda'

# 正则表达式的 基本用法，一个字符串，一个匹配规则
# 定义正则表达式
reg = '\d' # 找数字

res0 = re.fullmatch(reg,vars)
print(res0)

res1 = re.findall(reg,vars) # 直接获取结果，得到列表
print(res1)

res = re.finditer(reg,vars)
print(next(res))