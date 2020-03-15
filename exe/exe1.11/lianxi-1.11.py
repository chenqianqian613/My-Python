#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#创建一个有10个数字的列表,先输出此列表,然后再输出其中为偶数元素;
s1=list(range(1,15))
for a in s1:
    print(a)
print()
for a in s1:
    if(a%2==0):
        print(a)