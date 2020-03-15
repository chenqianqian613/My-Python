#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#初始化一个列表(1-20之间的整数) ;
# 然后 使用匿名函数,列表解析式, 来打印输出一个列表中的奇数;
def shuchujishu(list1):
    res=filter(lambda x:x%2!=0,list1)  #返回奇数
    print(list(res))
l=[2,4,3,5,6,7,8,9,1]
shuchujishu(l)
