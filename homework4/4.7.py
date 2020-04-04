#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#使用python代码统计一个文件夹中所有文件的总大小
import os
try:
    os.chdir(r"C:\Users\windows\PycharmProjects\homework4")
except FileNotFoundError:
    print('找不到指定文件！')

flist= os.listdir()

size=0
for i in flist:
    size1=os.path.getsize(i)
    size+=size1

print('该文件夹中所有文件大小为：',size)


