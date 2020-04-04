#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；
# 用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
#   提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
import time
from collections import deque
def lcounttime():
    t1=time.time()
    l1=[8,5,23,67,34,89,90,32]  #目前8个元素
    l1.insert(0,3)
    l1.append(56)
    time.sleep(3)    #程序运行时间过短，自行设置休眠3秒
    t2=time.time()
    lt=t2-t1
    print('列表自带函数计算时间为：',lt)
    return lt

def dcounttime():
    tt1=time.time()
    l2=deque([8,5,23,67,34,89,90,32])
    l2.appendleft(3)
    l2.append(56)
    time.sleep(3)
    tt2=time.time()
    dt=tt2-tt1
    print('deque集合类方法计算时间为：',dt)
    return dt

ltt=lcounttime()
dtt=dcounttime()
c=ltt-dtt
print('两种方法时间差为：',c)




