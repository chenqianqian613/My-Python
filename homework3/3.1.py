#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，
# 将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
import os
instr =[]
print("请输入任意行的文字信息：")
while(True):
    appe=[]
    str=input()
    if(len(str)!=0):
        appe.append(str)
        instr.append(appe)
    else:
        break
with open("input.txt","w") as f:
    for k in instr:
        f.write(' '.join(k))
        f.write("\n")
