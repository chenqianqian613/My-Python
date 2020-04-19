#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中
with open('running log.txt','w',encoding='utf-8') as f:
 def record(func):
    def diary(*args, **kw):
        print('调用函数 %s():' % func.__name__)
        f.write('调用了函数 %s()' % func.__name__)
        f.write("\n")
        return func(*args, **kw)
    return diary
 @record
 def now():
    print('2020-04-06')
 @record
 def last():
    print('2020-04-05')
 @record
 def future():
    print('2020-04-07')
 now()
 last()
 future()