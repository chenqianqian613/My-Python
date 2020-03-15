#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);
def paixv(list):
    list.sort()   #直接用sort函数
    print(list)

l1 = [3,4,5,2,89,67,45,34,22]
paixv(l1)
