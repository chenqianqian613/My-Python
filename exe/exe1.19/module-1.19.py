#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#练习:      将一个文件夹下的某个文件,拷贝到另外一个文件夹下去;
# 提示:
# 写一个copy函数，接受两个参数，第一个参数是源文件的位置，第二个#参数是目标位置，将源文件copy到目标位置。
# # 还需要判断一下这个文件之前是否存在
#
#提示2:  读源文件的内容;
#  创建目标文件;
# 读到的内容,再写入到目标文件
import os

def copy(p1,p2):                       #p1原文件地址，p2指定地址

    f1 = open(p1,'r',encoding='utf-8')

    f2 = open(p2,'w',encoding='utf-8')

    for i in f1:

        f2.write(i)                        #向新文件中写入数据

    f1.close()

    f2.close()


copy("copyin.txt","copyout2.txt")




