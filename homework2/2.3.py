#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#  数字列表请用随机数函数生成;
import random as ran
def jishu(shujv):
    print("数组中奇数为：")
    for num in shujv:
        if num % 2 != 0:
            print(num, end="  ")
r=[]
for k in range(1,30):
    k=ran.randint(1,100)
    r.append(k)
print("生成的数组为：\n{}".format(r))
jishu(r)
