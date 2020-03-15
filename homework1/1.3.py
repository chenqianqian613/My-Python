#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#定义2个列表，并初始化；
#找出这2个列表中，相同的元素并输出；
list1 = [3,6,9,23,'world','hello','fine','cqq']
list2 = ['hello',3,9,7,'fine']
for i in list1:
    for j in list2:
        if i == j:
            print(i)