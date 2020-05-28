#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 多进程练习：
# 计算1～100000之间所有素数的个数， 要求如下:
# - 编写函数判断一个数字是否为素数，然后统计素数的个数；
# -对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
# -对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
import time
from multiprocessing import Process,Pool

def is_prime(k):   #判断是否素数的函数
        for i in range(2, k):
            if k % i == 0 and k != 2:
                return False
        return True

def no_use():
    st=time.time()
    n=0
    for i in range(1,10001):   #只取值到10000个，便于测试，100000个运行时间太长
        if(is_prime(i)):
            n+=1
    et=time.time()
    t_no=et-st
    print('素数共有{0}个,不使用多进程用时{1}'.format(n,t_no))

def multy(n):
    sst=time.time()
    po = Pool(n)
    nn=0
    for i in range(1,10001):
        f=po.apply_async(is_prime,(i,))
        if(f.get()):
            nn+=1
    eet=time.time()
    t_use=eet-sst
    print('素数共有{0}个,使用{1}个多进程用时{2}'.format(nn,n,t_use))

if __name__ == '__main__':
    no_use()
    multy(4)
    multy(10)