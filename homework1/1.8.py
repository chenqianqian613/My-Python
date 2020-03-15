#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#设计一个数据结构，用来存放10个员工的信息并初始化，
# 每个员工信息包括：工号，姓名，工龄，工资；
# 将这10个员工，按照工资从高到低打印输出；
# 提示：可以组合使用我们的序列数据类型；
staff = [
 {'name':'李毅','number':120,'year':5,'price':6000},
 {'name':'王毅','number':121,'year':1,'price':2000},
 {'name':'张三','number':122,'year':3,'price':4500},
 {'name':'伍六','number':123,'year':3,'price':4000},
 {'name':'刘芳','number':124,'year':12,'price':12000},
 {'name':'张权','number':125,'year':2,'price':3000},
 {'name':'李四','number':126,'year':2,'price':2500},
 {'name':'王五','number':127,'year':10,'price':15000},
 {'name':'丁元','number':128,'year':3,'price':5600},
 {'name':'楚明','number':129,'year':7,'price':9200}]
staffqueue= sorted(staff,key = lambda x : x['price'],reverse = True)    #善于运用sorted函数的使用
for i in range(10):
 print(staffqueue [i])