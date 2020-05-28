#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 多进程通讯：
#   编写一个简单的聊天程序；
#   其中一个进程发送文字聊天消息（从键盘输入文字消息）；
#   另外一个进程接收并打印消息；
from multiprocessing import Process, Queue
import time


def send(n,message):
    n.put(message)
    time.sleep(2)

def receive(n):
    while (True):
        receivemessage = n.get(True)
        print('接收到以下消息:%s' % receivemessage)


if __name__ == '__main__':
    n = Queue()
    s = input('请输入要发送的消息：')
    sth = Process(target=send, args=(n, s))
    sth.start()
    rth = Process(target=receive, args=(n,))
    rth.start()
    sth.join()
    rth.terminate()