#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)
def cacluate(v1,v2,f):
    if(f == '+'):
        return v1+v2
    elif(f == '-'):
        return v1-v2
    elif(f == '*'):
        return v1*v2
    elif(f == '/'):
        if(v2 == 0):
            return 'false'  #考虑分母为0的错误情况
        else:
            return v1/v2
    else:
        return 'false'

print('请输入两个数字：')
v1,v2 = map(int,input().split())
f = input('请输入要进行的运算(+,-,*,/):')
print('计算结果为:',cacluate(v1,v2,f))
