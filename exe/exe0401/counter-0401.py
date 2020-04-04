#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#

#定义一个高阶函数, 实现加,减,乘,除计算器功能；

def jia(a, b):
    print(a + b)

def jian(a, b):
    print(a - b)

def cheng(a, b):
    print(a * b)

def chu(a, b):
    print(a / b)


if __name__ == '__main__':
    v1 = int(input("请输入第一个数的值："))
    v2 = int(input("请输入第二个数的值："))
    print('请选择要进行的运算：+-*%')
    s=input()
    if s=='+':
        print('运算结果为：')
        jia(v1,v2)
    if s=='-':
        print('运算结果为：')
        jian(v1,v2)
    if s=='*':
        print('运算结果为：')
        cheng(v1,v2)
    if s=='%':
        print('运算结果为：')
        chu(v1,v2)


