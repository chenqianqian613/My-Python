#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#编写一个函数,接收n个数字，求这些参数数字的和;
def shu(*number):
    n = 0
    for i in number:
        n = i + n
    print('和为:',n)

shu(8,14,35,42,6,9)