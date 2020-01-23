#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 插入排序.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/19 13:53

nums = [5,3,6,4,1,2,8,7]
for i in range(1,len(nums)): # 遍历整个列表，遍历未排序
    for j in range(i): # 遍历已经排序过的列表
        if nums[j] > nums[i]:
            ins = nums[i]
            nums.remove(nums[i])
            nums.insert(j,ins) # 把较小的元素插入到元素 j 的前面
            break
print(nums)