#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#对参考文档进行小修改和测试
import socket
import threading
import os
import get #调用get模块

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#addr = # 服务器端的IP和端口
addr = (get.get_ip(), 10000)  #只有本机做测试时
s.connect(addr)


def recv_msg():  #
    print("连接成功！现在可以接收消息！\n")
    while True:
        try:  # 测试发现，当服务器率先关闭时，这边也会报ConnectionResetError
            response = s.recv(1024)
            print(response.decode("gbk"))
        except ConnectionResetError:
            print("服务器关闭，聊天已结束！")
            s.close()
            break
    os._exit(0)


def send_msg():
    print("连接成功！现在可以发送消息了！\n")
    print("输入消息按回车来发送")
    print("输入esc来退出聊天")
    while True:
        msg = input()
        if msg == "esc":
            print("你退出了聊天")
            s.close()
            break
        s.send(msg.encode("gbk"))  #用gbk读取
    os._exit(0)


threads = [threading.Thread(target=recv_msg), threading.Thread(target=send_msg)]
for t in threads:
    t.start()