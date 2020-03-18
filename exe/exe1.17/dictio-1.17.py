#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#练习6：给定一个字典,保存了5个同学的学号,姓名,年龄;使用pickle模块将数据对象保存到文件中去;
import pickle
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

output = open(r'C:\Users\windows\Desktop\yyy\output', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
output.close()