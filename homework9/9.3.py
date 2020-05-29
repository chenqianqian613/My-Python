#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
import socket
import threading

#多线程例题,需用网络调试工具配合测试
def client(udp_socket):
    """获取键盘数据，并将其发送给对方"""
    while True:
        # 1. 从键盘输入数据
        msg = input("\n请输入要发送的信息:")
        # 2. 输入对方的ip地址
        dest_ip = input("\n请输入对方的ip地址:")
        # 3. 输入对方的port
        dest_port = int(input("\n请输入对方的端口号:"))
        # 4. 发送数据
        udp_socket.sendto(msg.encode("utf-8"), (dest_ip, dest_port))


def server(udp_socket):
    """接收数据并显示"""
    while True:
        # 1. 接收数据
        recmsg = udp_socket.recvfrom(1024)
        # 2. 解码
        recip = recmsg[1]
        recmsg = recmsg[0].decode("utf-8")
        # 3. 显示接收到的数据
        print(">>>来自客户端%s:%s" % (str(recip), recmsg))


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定本地信息
    udp_socket.bind(("192.168.1.3",8862))

    # 3. 创建一个子线程用来接收数据
    t = threading.Thread(target=server, args=(udp_socket,))
    t.start()
    # 4. 让主线程用来检测键盘数据并且发送
    client(udp_socket)

if __name__ == "__main__":
    main()

