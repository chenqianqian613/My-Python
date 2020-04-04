#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#通过Python来模拟实现一个txt文件的拷贝过程
import os

def copy(p1,p2):                       #path原文件地址，path1指定地址

    f1 = open(p1,'r',encoding='utf-8')

    f2 = open(p2,'w',encoding='utf-8')

    for i in f1:

        f2.write(i)                        #向新文件中写入数据

    f1.close()

    f2.close()


copy("title.txt","title2.txt")

#方法2:直接用shutil模块
# shutil模块是一个文件、目录的管理接口，提供了一些用于复制文件、目录的函数
# copyfile()函数可以实现文件的拷贝
# copyfile(src, dst)
# move()函数实现文件的剪切
# move(src, dst)

#import shutil

#shutil.copyfile("hello.py", "hello2.py")  # hello.txt内容复制给hello2.txt
#shutil.move("hello.py", "../")  # hello.txt复制到当前目录的父目录，然后删除hello.txt
#shutil.move("hell2.txt", "hello3.txt")  # hello2.txt移到当前目录并命名为hello3.py, 然后删除hello2.txt