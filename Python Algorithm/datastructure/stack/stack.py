#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: stack.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2019/10/8 18:50

# 定义一个栈
class Stack(object):
    def __init__(self, limit=10):
        self.stack = []  # 存放元素
        self.limit = limit  # 栈容量极限
# 元素进栈
    def push(self,data):
        if len(self.stack) >= self.limit:
            raise IndexError("超出栈容量极限")
        self.stack.append(data)
# 元素出栈
    def pop(self):
        if self.stack: # 还有元素
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")
# 添加其它函数
    def peek(self):#查看栈顶元素
        if self.stack:
            return self.stack[-1] #返回末尾元素
        else:
            raise IndexError("栈为空")

    def stack_bottom(self):#查看栈底元素
        if self.stack:
            return self.stack[0]
        else:
            raise IndexError ("栈为空")

# 栈空
    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        if self.stack:
            return len(self.stack)
        else:
            raise IndexError("栈为空")