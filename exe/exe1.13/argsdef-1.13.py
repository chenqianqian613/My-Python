#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#使用不定长参数定义一个函数;
# 实现对输入数据的封装(封装成一个列表和字典),然后打印输出;
def fun(x,**args):
    print("列表为：",x)
    print("字典为：",args)
fun(1, a=2,b=3)