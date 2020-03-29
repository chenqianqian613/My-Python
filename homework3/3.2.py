#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx
import os
import sys
str=[]
try:
    with open("input.txt")as f:
        for n,v in enumerate(f):
            app=[v.strip()]
            str.append(app)
            print("第{0}行：{1}".format(n+1,v))
except FileNotFoundError as err:
    print("未找到文件")

