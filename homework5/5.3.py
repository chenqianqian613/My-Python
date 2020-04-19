#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）

def identificantion(func):
 def login():
    users={}
    with open('users.txt')as f:
     for i in f.readlines():
        users[i.split(' ')[0]] = i.split(' ')[1].strip()
    name = input("请输入账号：")
    if (name in users.keys()):
        passWord = input("请输入密码：")
        if (users[name] == passWord):
            func()
        else:
            print('密码错误！无法调用函数')
    else:
        print('账号不存在，请确认后输入！')
 return login()
@identificantion
def func():
    print('认证成功，可以调用函数了。')



