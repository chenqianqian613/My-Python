#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 使用random模块，生成随机数，来初始化一个列表，元组；
#      使用了 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法；
import random
liebiao = [random.randint(1, 100) for i in range(10)]
yuanzu = tuple([random.randint(1, 100) for i in range(10)])
print(f"生成的随机数列表如下：{liebiao}\n")
print(f"生成的随机元组如下：{yuanzu}\n")