#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#字典的元素的增加, 修改,删除; 并观察输出
dict = {'Name': 'Alice', 'Age': 17, 'Class': 'Class8'}
dict['Age'] = 19  # 更新 Age
dict['School'] = "NCEPU"  # 添加信息
del dict['Name'] # 删除键 'Name'
#dict.clear()     清空字典
#del dict         删除字典
print(dict['Age'])
print(dict)