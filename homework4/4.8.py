#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#京东二面笔试题
# 1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的ip地址;
# 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
import random

def create():
    with open("ip.txt", "w") as f:
        for i in range(1200):
            iplist = "172.25.254." + str(random.randint(0, 255))
            f.write(iplist + '\n')


def count():
    ipdic = {} #字典
    with open("ip.txt", "r") as f:
        for i in f:
            i = i.strip('\n')   #去掉换行符
            ips = i.split(".")[3]
            if ips not in ipdic:
                ipdic[ips] = 1    #若未出现过，计入，初值为1
            else:
                ipdic[ips] += 1   #若已存在，在原基础上加一
    iplist = [(k, v) for k, v in ipdic.items()]  #把统计出的字典转化成列表
    return iplist

if  __name__ == '__main__':
    create()
    ipl=count()
    ipl.sort(key=lambda k: k[1], reverse=True)
    ipl = ipl[0: 10]
    print("出现频率前十的ip地址为：(频率从高到低)")
    for k in ipl:
       print("172.25.254.{}".format(k[0]))
