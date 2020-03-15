#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#定义一个函数, 打印输出n以内的斐波那契数列;
def Fibonacci(n):
    a = 0
    b = 1
    print(f"{a}", end = ' ')
    while b < n:
        print(f"{b}", end = ' ')
        b,a = b + a, b

num = input("请输入n的值：")
Fibonacci(int(num))