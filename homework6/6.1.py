#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 定义一个狗类,里面有一个 列表成员变量(列表的元素是字典),
# 分别记录了 3种颜色的狗的颜色, 数量,和价格;
# 实现狗的买卖交易方法;
# 打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
class dog():
    dogs = [{'color':'red','num':5,'price':1200},
          {'color':'blue','num':4,'price':1500},
          {'color':'black','num':3,'price':2200}
    ]
    def buy(self,cc):
        for i in self.dogs:
         if i['color']==cc:
            i['num']+=1
            print('You buy a %s dog'%cc)
    def sell(self,c):
        for i in self.dogs:
            if i['color']==c:
                i['num']-=1
                print('You sell a {} dog, get {} money'.format(i['color'],i['price']))
d=dog()
d.buy('red')
d.buy('blue')
d.buy('blue')
d.sell('black')
d.sell('red')
for i in d.dogs:
    print('color:{0}  num:{1}'.format(i['color'],i['num']))


