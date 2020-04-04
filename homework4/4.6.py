#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小;
# 格式效果如下:
#     名称         日期                   类型（文件夹或者 文件）       大小
import os

try:
    os.chdir("homework4")
except FileNotFoundError:
    print('找不到指定文件！')

flist= os.listdir()

print("名称\t\t日期\t\t类型\t\t大小")
for i in flist:
    name = i
    date = os.path.getctime(i)
    type = ''
    if os.path.isdir(i):
        type = '文件夹'
    else:
        type = '文件'
    size = os.path.getsize(i)
    print(f'{name}\t{date}\t{type}\t{size}')

