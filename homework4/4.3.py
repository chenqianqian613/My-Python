#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
#         Tom   admin   XXXXX
#         Jack   root      XXXXX
import hashlib


with open ('zhanghao.txt','w', encoding = 'utf-8') as f:
    for i in range(5):
        name,zhanghao,pwd=input('请输入一名学生的姓名，账号和密码（用空格隔开）').split()
        md5=hashlib.md5()
        md5.update(pwd.encode('utf-8'))
        pwd2=md5.hexdigest()
        f.writelines(f'{name}\t{zhanghao}\t{pwd2}\n')
