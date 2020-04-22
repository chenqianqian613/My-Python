#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#

class ddd(object):
    n=1
    def __init__(self):
        self.n=ddd.n
        self.blood=80
        self.strong=35  #设置为15会出错
        ddd.n+=1
    def attack(self,people): #被袭击
        self.blood-=people.strong
        self.strong-=3