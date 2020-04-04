#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# (继续第三题的练习)
# 模拟用户登录:
# 5个同学的姓名, 账号和密码(加密后的), 保存在一个文件上;
#系统提示, 请输入登录同学姓名, 正确后, 请输入账号, 正确后, 提示请输入密码（输入明文）;
# 如果都正确, 打印提示, 您登录成功(失败);
import hashlib
import os
nlist=[]
zlist=[]
plist=[]
with open('zhanghao.txt','r',encoding='utf-8') as f:
    hangshu=f.readlines()
    for k in hangshu:
        k.strip("\n")
        stu = k.split()
        nlist.append(stu[0])
        zlist.append(stu[1])
        plist.append(stu[2])

print('请输入姓名：')
sname=input()
if sname in nlist:
    position=nlist.index(sname)
    print('请输入账号')
    szhanghao=input()
    if szhanghao==zlist[position]:
        print('请输入密码')
        spwd=input()
        md5=hashlib.md5()
        md5.update(spwd.encode('utf-8'))
        pwd3 = md5.hexdigest()
        if pwd3 == plist[position]:
            print('登陆成功！')
        else:
            print('密码错误，登录失败！')
    else:
        print('账号不匹配！')
else:
    print('无此人名！请检查后输入。')