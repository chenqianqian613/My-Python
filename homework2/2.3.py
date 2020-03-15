#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#  数字列表请用随机数函数生成;
import random as rd
def jishu(shujv):
    print("数组中奇数为：")
    for num in shujv:
        if num % 2 != 0:
            print(num, end="  ")


if __name__ == '__main__':
    randomsj = [rd.randint(1, 1000) for i in range(1, 20)]
    print("生成的数组为：\n{}".format(randomsj))
    jishu(randomsj)