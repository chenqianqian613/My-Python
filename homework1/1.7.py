#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#打印输出9*9乘法表
for k in range(1,10):
    for h in range(1,k+1):
        print(f'{h}*{k}={k*h}', end="  ")
    print("\n")
