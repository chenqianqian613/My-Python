#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#提示输入需要购买的苹果的重量(斤),然后提示输入每斤的价格,请计算应支付的总价,并打印提示输出;
a=int(input('请输入想要购买的苹果斤数：'))   #python3 里input() 默认接收到的是 str 类型。要强制类型转换！
b=int(input('请输入苹果的单价：'))
c=a*b
print('您购物的总价为：',c)