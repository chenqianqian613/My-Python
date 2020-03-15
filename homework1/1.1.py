#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
p = [2,]
for i in range(2,50):
    for j in range(2,i):
        if i % j == 0:
            break
        if j == i-1:
            p.append(i)
print('奇数有：', [x for x in range(50) if x % 2 != 0])
print('偶数有：', [x for x in range(50) if x % 2 == 0])
print('质数有:',p)
print('同时被2,3整除的数有：',[x for x in range(50) if x % 2 == 0 and x % 3 == 0])