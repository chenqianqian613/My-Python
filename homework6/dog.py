#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# class dogs(object):
#     num=1
#     def __init__(self):
#         self.n=dogs.num
#         self.blood=80
#         self.gongjili=15
#         dogs.num+=1  #每创建一个，狗的数量加一
#     def gongji(self,people):
#         self.blood-=people.dajili
#         self.gongjili-=3
class ddd(object):
    num=1
    def __init__(self):
        self.num=ddd.num
        self.blood=80
        self.strong=35  #设置为15会出错
        ddd.num+=1
    def attack(self,people): #被袭击
        self.blood-=people.strong
        self.strong-=3