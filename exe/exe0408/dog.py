#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 定义一个dog类(颜色, 名称), 里面有一个狗叫的方法;
# 不同的狗叫声可能不一样;
# 然后实例化几条狗, 然后统计实例化狗的数量

class dog(object):
    voice=''
    n=0
    def __init__(self,voice):
        self.voice=voice
        dog.n+=1
    def dogvoice(self):
        print('%s在叫'%(self.voice))
d1=dog('贵宾')
d1.dogvoice()
d2=dog('泰迪')
d2.dogvoice()
d3=dog('金毛')
d3.dogvoice()
d4=dog('哈士奇')
d4.dogvoice()
print('实例化狗的数量为：',d4.n)


