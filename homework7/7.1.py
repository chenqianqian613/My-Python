#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 给定一个文件webspiderUrl.txt，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
#    提示，文件有1000行，注意控制每次读取的行数；
import re
r = re.compile(r"http://www.[a-zA-Z0-9\.\-\_]{0,25}")
with open(r"webspiderUrl.txt", "r", encoding="utf-8") as f1:
    with open(r"totalurl.txt", "w") as f2:
        for lines in f1:
            rs = r.findall(lines)
            for i in rs:
                f2.write(i)
                f2.write('\n')
