#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数);
# 然后按照分数从高到低进行排序输出
import os

grade=[]
try:
    with open("student.txt",'r', encoding = 'utf-8') as f:
        lines=f.readlines()
except FileNotFoundError as err:
        print("未找到文件")
else:
    for k in lines:
        grade.append(k.strip().split('\t'))
    sortgrade=sorted(grade[1:-1],key=lambda student: int(student[2]))
    for i in sortgrade:
        print(' '.join(i))

