#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 编写装饰器来实现，对目标函数进行装饰，分3种情况：
# 目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
#      三个目标函数分别为：
#      A 打印输出20000之内的素数；
#      B 计算整数2-10000之间的素数的个数；
#      C 计算整数2-M之间的素数的个数；
def wcwf(func):
    def inner():
        print('这是无参数无返回值的装饰器')
        func()
    return inner()
def yfwc(func):
    def inner():
        print('这是有返回值的装饰器')
        re=func()
        return re
    return inner
def ycyf(func):
    def inner(*arg, **kws):
        print('这是有参数有返回值的装饰器')
        result = func(*arg, **kws)
        return result
    return inner
def judge(k):
    for i in range(2,k):
        if k%i==0:
            return False
        else:
            return True
@wcwf
def A():
    for i in range(1, 20000):
        if judge(i):
            print('{}'.format(i), end='\t')
    else:
        print('\n')
@yfwc
def B():
    count = 0
    for i in range(2,10000):
        if judge(i):
            count+=1
    return count
@ycyf
def C(M):
    count = 0
    for i in range(2, M):
        if judge(i):
            count += 1
    return count
A
print('2-10000之间的素数有%s个'%B())
print('\n')
print('300以内的素数有%s个'%C(300))

