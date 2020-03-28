#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#练习6：给定一个字典,保存了5个同学的学号,姓名,年龄;使用pickle模块将数据对象保存到文件中去;
import os
import pickle
data1 = [
    {'num': '121', 'name': 'amy', 'age': 19},
    {'num': '122', 'name': 'alice', 'age': 19},
    {'num': '123', 'name': 'sam', 'age': 17},
    {'num': '124', 'name': 'tom', 'age': 18},
    {'num': '125', 'name': 'linda', 'age': 20}
]
with open('D:\My-Python\exe\exe1.17\pickle1', 'wb') as f:
    pickle.dump(data1, f)
with open('D:\My-Python\exe\exe1.17\pickle1', 'rb') as f:
    ldata1 = pickle.load(f)
    print(ldata1)
