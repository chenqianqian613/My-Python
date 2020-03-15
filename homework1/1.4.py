#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#判断用户输入的年份是否为闰年
#四年一闰，百年不闰，四百年大闰
runnian = int(input("输入需要判断的年份:"))
if runnian % 4 == 0:
    if runnian % 100 == 0 and runnian % 400 != 0:
        print("所查询年份不是闰年")
    else:
        print("所查询年份是闰年")
else:
    print("所查询年份不是闰年")