#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#前面2个元素为0，1，输出100以内的斐波那契数列；
y1 = 0
y2 = 1
print(y1)
print(y2)
for i in range(1,100):
    if i == y1 + y2:
        print(i)
        y1,y2 = y2,i
