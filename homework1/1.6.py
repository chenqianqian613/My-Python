#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#前面2个元素为0，1，输出100以内的斐波那契数列；
v1 = 0
v2 = 1
print(v1)
print(v2)
for i in range(1,100):
    if i == v1 + v2:
        print(i)
        v1,v2 = v2,i