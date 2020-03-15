#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；
#我设置为猜8次
import random
m = random.randint(1,20)
for i in range(8):          #猜8次
    x = int(input("这是猜数字第%d次："%(i+1)))
    if x == m:
        print('猜对了！')
        break
    elif i == 8 and x!= m:
        print('对不起您未猜对数字，正确答案为：',m)