#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#文件编程小项目
import os
para='''
How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind
'''
#要注意不同的操作时使用多个打开文件语句，否则容易出现读取方式不符合等错误
with open("Blowing in the wind.txt","w")as f:
    f.write(para)
with open("Blowing in the wind.txt") as f:
    lines = f.readlines()          #如果写打开模式，会因为不是字节无法读取
    t=[line.strip()for line in lines]   #strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    t.insert(0,'Blowing in the wind')    #注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
    t.insert(1,'Bob Dylan')
    t.insert(-1,'1962 by Warner Bros.Inc.')
with open("Blowing in the wind.txt")as f:
    print(f.read())