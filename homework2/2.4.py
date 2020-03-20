#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
def count(s):
    num = 0
    ch = 0
    sp = 0
    ot = 0
    for k in s:
        if k.isdigit():
            num += 1
        elif k.isalpha():
            ch += 1
        elif k == ' ':
            sp += 1
        else:
            ot += 1
    print('总共有数字%d个' %num)
    print('总共有字母%d个' %ch)
    print('总共有空格%d个' %sp)
    print('总共有其他字符%d个' %ot)
s1 = input('请输入一串字符:')
count(s1)
