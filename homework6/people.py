#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
class ppp(object):
    n=1
    def __init__(self):
        self.n=ppp.n
        self.blood=100
        self.strong=40 #设置为10会出错
        ppp.n+=1
    def attack(self,dog):
        self.blood-=dog.strong
        self.strong-=2