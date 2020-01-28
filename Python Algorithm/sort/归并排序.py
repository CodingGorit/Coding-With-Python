#!/usr/bin/python
# -*- coding: utf-8 -*-
#file: 归并排序.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/1/27 21:52

nums = [5,3,6,4,1,2,8,7]

def MergeSort(num):
    if(len(num)<=1): 				#递归边界条件
        print(num)
        return num 				# 到达边界时返回当前的子数组
    mid = int(len(num)/2) 			#求出数组的中
    llist,rlist = MergeSort(num[:mid]),MergeSort(num[mid:])#调用函数分别为左右数组排序
    result = []
    i,j = 0,0

    while i < len(llist) and j < len(rlist): #while循环用于合并两个有序数组
        if rlist[j]<llist[i]:
            result.append(rlist[j])
            j += 1
        else:
            result.append(llist[i])
            i += 1
    result += llist[i:]+rlist[j:] 	#把数组未添加的部分加到结果数组末尾
    return result 					#返回已排序的数组

print(MergeSort(nums))
