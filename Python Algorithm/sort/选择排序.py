#!/usr/bin/python
# -*- coding: utf-8 -*-
# file: 选择排序.py
# @author: Gorit
# @contact: gorit@qq.com
# @time: 2020/1/19 14:02

def basic_choose(nums):  # 使用两个数组完成
    res = list ()  # 使用全局数组
    while len (nums):  # 判断是否所有元素都进入了循环
        minlnd = 0  # 初始化最小的元素值
        for i in range (1, len (nums)):  # 使用循环遍历查找到最下的元素的值
            if nums[minlnd] > nums[i]:  # 使用循环找到列表中的最小值
                minlnd = i
        res.append(nums.pop (minlnd))
    print(res)


def advanced_choose(nums):
    for i in range(len(nums)-1):
        minland = i
        for j in range(i,len(nums)):
            if nums[j]<nums[minland]:
                minland = j  # 找到循环中的最小值
        nums[i],nums[minland] = nums[minland],nums[i]
    return nums

if __name__ == '__main__':
    nums = [5, 3, 6, 4, 1, 2, 8, 7]
    # basic_choose(nums=nums)
    res = advanced_choose(nums=nums)
    print(res)