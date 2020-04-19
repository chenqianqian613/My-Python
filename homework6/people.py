#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# class peoples(object):
#     num=1
#     def __init__(self):
#         self.num=peoples.num
#         self.blood=100
#         self.dajili=30
#         peoples.num+=1
#     def daji(self,dog):
#         self.blood-=dog.gongjili
#         self.dajili-=2
class ppp(object):
    num=1
    def __init__(self):
        self.num=ppp.num
        self.blood=100
        self.strong=40 #设置为10会出错
        ppp.num+=1
    def attack(self,dog):
        self.blood-=dog.strong
        self.strong-=2