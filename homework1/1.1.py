#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；


p = [2,]
o =[]
j =[]
h =[]
for m in range(2,50):#不从0开始，以免出现分子或分母为0的异常错误，且0-50内质数从2开始
    for n in range(2,m):
        if m % n == 0:
            break
        if n == m-1:
            p.append(m)
for i in range(0,50):
    if (i%2) !=0:
        j.append(i)
for k in range(0,50):
    if (k%2) ==0:
        o.append(k)
for t in range(0,50):
    if (t%2)==0 and (t%3)==0:
        h.append(t)
print('0-50中偶数有：', o)
print('0-50中奇数有：', j)
print('0-50中质数有:',p)
print('0-50中同时被2,3整除的数有：',h)

