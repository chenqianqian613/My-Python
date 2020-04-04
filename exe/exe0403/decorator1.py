#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
import time
def yunxingrizhi(c):
    def inner():
        t1=time.time()
        c()
        t2=time.time()
        print('Total time is:',t2-t1)
        print('加法被执行了')
    return inner
@yunxingrizhi
def jiafa():
    print('请输入第一个数字')
    a=int(input())
    print('请输入第二个数字')
    b=int(input())
    r=a+b
    print('加法结果为：',r)

jiafa()
