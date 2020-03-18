#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 练习3:   一个文件内容的如下,请读取文件的内容, 并输出;
#             姓名      学号      分数
#             张三      101         78
#             李四      102         87
#             王五       103        83
f = open(r'C:\Users\windows\Desktop\yyy\new 1', 'r', encoding='utf-8')   #open的encoding要改成utf8

print(f.read())
f.close()