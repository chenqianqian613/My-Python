#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；
#我设置为猜9次
import random
m = random.randint(1,20)#1--20内的随机数
for n in range(9):          #猜9次
    k = int(input("请输入您第%d次要猜的数字："%(n+1)))  #强制类型转换,n+1使显示次数不从0开始
    if k == m:
        print('猜对了！')
        break
    elif n == 8 and k != m:
        print('对不起您未猜对数字')
        print('The Correct answer is :',m)
