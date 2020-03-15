#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#定义一个函数,来计算苹果的价格(重量*价格); 通过键盘输入重量和价格,然后调用函数来计算;
def sumprice(a,b):
    c=a*b
    print('苹果的总价为：',c)
m=int(input('请输入苹果的单价：'))
n=int(input('请输入苹果的重量：'))
sumprice(m,n)
