#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#  题目要求：
#  在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
#  将当前img目录所有以.png结尾的后缀名改为.jpg.
#
import os

try:
  os.chdir(r'C:\Users\windows\PycharmProjects\homework3\img')   #直接打开创建好的目录
except FileNotFoundError as err:
        print("未找到文件")
else:
 files=os.listdir()
 for f in files:
    if f.endswith(".png"):
        fff = os.path.splitext(f)   #splitext方法分离文件名与扩展名

        if fff[1] == '.png':
                new = fff[0] + '.jpg'
                os.rename(f, new)