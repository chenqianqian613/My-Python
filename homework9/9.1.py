#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 将“网络编程”章节中课件中的例子，在本机测试运行；下载安装网络编程调试工具；
import socket
def main():
    # 1 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 准备接收方的地址 使用udp套接字发送数据:发什么,发给谁
    # '192.168.1.24'表示目的ip地址
    # 8888表示目的端口
    dest_addr = ('192.168.1.3', 8888)  # 注意 是元组，ip是字符串，端口是数字
    #注意用网络调试工具调试时不要同时占用多个端口，会打不开或连接不上，及时关闭后台不需要的调试端口。
    # 3. 从键盘获取数据
    send_data = input("请输入要发送的数据:")  #输入中文调试工具接收到会乱码
    # 4. 发送数据到指定的电脑上的指定程序中
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

    # 5 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()

# from socket import *
#
#
# def main():
#     # 绑定端口信息
#     udp_socket = socket(AF_INET, SOCK_DGRAM)
#
#     local_addr = ('', 8080)
#
#     udp_socket.bind(local_addr)
#     # 接收数据
#     recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
#     # 打印显示接收到的数据
#     print(recv_data)
#
#     # print(recv_data[0].decode('gbk'))
#     # print(recv_data[1])
#
#     # 关闭套接字
#     udp_socket.close()
#
#
# if __name__ == "__main__":
#     main()