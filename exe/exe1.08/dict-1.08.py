#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#定义一个字典,存放某个同学的信息(学号,姓名,班级,年龄);
# 再定义另外一个字典,存放5个同学的学号,姓名信息;
#    通过键来访问相应的数据; 或者整体输出
dict1={'num':25,'name':'Alice','class':'class7','age':18}
dict2={'num1':23,'name1':'amy',
       'num2':24,'name2':'tom',
       'num3':27,'name3':'sam',
       'num4':26,'name4':'linda',
       'num5':29,'name5':'liming'}
print(dict1['class'])
print(dict1)
print(dict2['name3'])
print(dict2)