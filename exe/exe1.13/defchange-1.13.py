#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#定义一个函数,  打印输出列表里面的元素;  然后增加列表中的元素, 然后再输出新的列表;
# 主程序中,打印这个列表的地址(传参之前,传参之后);
def change(b):
    print("重新赋值之前的地址：",id(b))
    b=10
    print("重新赋值之后的值：",b)
    print("重新赋值之后的地址：",id(b))

c=2
print("c的地址：",id(c))
change(c)
print("传了参数之后c的地址：",id(c))
print("c的值：",c)