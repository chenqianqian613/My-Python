#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 定义一个函数，判断一个输入的日期，是当年的第几周，周几？
# 将程序改写一下，能针对我们学校的校历时间进行计算
# （校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；

from datetime import date
from datetime import datetime
from datetime import timedelta

def judgeweek(date):   #从年初开始
    weekdate=date.isocalendar()  #isocalender()返回指定日期的年，第几周，周几这三个值。
    print('输入的日期是{}年的第{}周'.format(weekdate[0],weekdate[1]))

def ncepuweek(date1):  #按照校历，2.16开学，距离2020.1.1相差47天
    dategap=timedelta(days=47)
    judgedate=date1-dategap
    ncepudate=judgedate.isocalendar()
    print('输入的日期是本学期的第{}周'.format(ncepudate[1]))



print('请输入要判断的日期：（用-号分隔年月日）:')
inputtime=input()
sdate=datetime.strptime(inputtime,"%Y-%m-%d")
judgeweek(sdate)
ncepuweek(sdate)
