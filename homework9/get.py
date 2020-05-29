#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
import socket
import datetime
#对参考文档进行小修改和测试

def get_ip():
    """用来搞到IP"""
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip


def get_time():
    """得到发送时间"""
    now = datetime.datetime.now()
    send_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return send_time