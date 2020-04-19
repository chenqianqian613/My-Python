#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 练习:
# 题目1：匹配出163的邮箱地址，且@符号之前有4到20位英文或者数字字符，例如hello@163.com
import re
# emaillist=["chenqianqian@163.com","wangying@163.cnosdd",".laowng.lao@sohu.com"]
#
# for email in emaillist:
#     ret=re.match('[\w]{4,20}@163\.com$',email)
#     if ret:
#         print('%s符合邮件规定地址，re.match匹配的结果是：%s'%(email,ret.group()))
#     else:
#         print('%s不是符合规定的邮件地址'%email)

email=input('请输入一个要判断的邮件地址：')
ret=re.match('[\w]{4,20}@163\.com$',email)
if ret:
        print('%s符合邮件规定地址，re.match匹配的结果是：%s'%(email,ret.group()))
else:
        print('%s不是符合规定的邮件地址'%email)
