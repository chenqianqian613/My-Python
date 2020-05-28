#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 有100个同学的分数：数据请用随机函数生成；
#      A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#      B 利用线程池来实现；
# import random
# import threading
# import time
# A法：
# grades = [random.randint(30,100) for i in range(100)]  #随机生成100位同学分数,分数在30--100之间
# def th1():
#     for i in range(0,19):
#         print('th1:')
#         print(grades[i])
#
# def th2():
#     for i in range(20,39):
#         time.sleep(1)
#         print('th2:')
#         print(grades[i])
#
# def th3():
#     for i in range(40,59):
#         time.sleep(2)
#         print('th3:')
#         print(grades[i])
#
# def th4():
#     for i in range(60,79):
#         time.sleep(2)
#         print('th4:')
#         print(grades[i])
#
# def th5():
#     for i in range(80,99):
#         time.sleep(2)
#         print('th5:')
#         print(grades[i])
#
# if __name__ == '__main__':
#     t1=threading.Thread(target=th1)
#     t1.start()
#     t2=threading.Thread(target=th2)
#     t2.start()
#     t3=threading.Thread(target=th3)
#     t3.start()
#     t4=threading.Thread(target=th4)
#     t4.start()
#     t5=threading.Thread(target=th5)
#     t5.start()

#B法：
from multiprocessing import Pool
import time
import random
grades = [random.randint(30,100) for i in range(100)]
def grade(s,e):
    for i in range(s,e):
        print(grades[i])
        time.sleep(2)  #设置为sleep（1）时，时间不够，容易出错

if __name__ == '__main__':
    po = Pool(5)
    po.apply_async(grade,(0,19))
    po.apply_async(grade,(20,39))
    po.apply_async(grade,(40,59))
    po.apply_async(grade,(60,79))
    po.apply_async(grade,(80,99))
    po.close()  # 关闭进程池
    po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
    print('输出完成')