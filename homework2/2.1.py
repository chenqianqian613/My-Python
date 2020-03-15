#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
def length(a):
    return len(a)  #len() 方法返回对象（字符、列表、元组等）长度或项目个数。

num = eval(input('请输入字符串，列表或者元组'))  #eval函数就是实现list、dict、tuple与str之间的转化
print('长度为:',length(num))