#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#定义一个函数, 打印输出n以内的斐波那契数列;
def fff(k):
    v1 = 0
    v2 = 1
    print(f"{v1}", end=' ')
    while v2 < k:
        print(f"{v2}", end=' ')
        v2,v1 = v2 + v1, v2

n2=input("请输入n的值：")
fff(int(n2))
