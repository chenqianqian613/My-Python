#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#定义一个集合类型的变量(用2种方法初始化),然后进行相应的 元素的操作;
fruit = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
set1=set('blue')
fruit.add('strawberry')
fruit.remove('pear')
set1.update('yellow')
set1.update('red')
set1.discard('blue')
print(set1)
print(fruit)