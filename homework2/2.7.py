#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;
#     A---成绩>=90;
#     B-->成绩在 [80,90)
#     C-->成绩在 [70,80)
#     D-->成绩<70
import random as r
def pingji(score):
    dengji = {}
    for k, v in score.items():
        if v <= 100 and v >= 90:
            dengji[k] = 'A'
        elif v < 90 and v >= 80:
            dengji[k] = 'B'
        elif v < 80 and v >= 70:
            dengji[k] = 'C'
        else:
            dengji[k] = 'D'
    return dengji



s1 = {}
for i in range(20):
    s1['学生%d' % (i + 1)] = r.randint(36, 100)  #生成的随机分数定在30--100之间
print("学生的成绩为：\n{}".format(s1))
dj = pingji(s1)
print("\n学生的等级为：\n{}".format(dj))
