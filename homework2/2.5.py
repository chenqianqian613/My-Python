#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;
def l(dic):
    for key,value in dic.items():
        if len(value) > 2:
            dic[key] = value[0 : 2]
    return dic

dic = {'a':'37293729','b':'25','c':'shigais','d':'343','e':'cqqruanjian'}
print(l(dic))
