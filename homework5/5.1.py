#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#编写一个装饰器，能计算其他函数的运行时间
import time, random
def outer(fc):  # 将index的地址传递给func
    def inner():
        time1 = time.time()
        fc()   # fun = index  即func保存了外部index函数的地址
        time2 = time.time()
        print("运行时间为%s"%(time2 - time1))
    return inner  # 返回inner的地址

@outer
def test():
    time.sleep(random.randrange(1, 5))
    print("计算结束")

test()