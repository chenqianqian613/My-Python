#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，
# 并打印出该字符及其出现的次数。
#  例如，输入 aaaabbc，输出：a:4
from collections import  Counter

def max(t1):
    return Counter(t1).most_common(1)
    # most_common(n) 按照counter的计数，按照降序，返回前n项组成的list; n忽略时返回全部
    #此处只返回前1项，也就是第一项

text = "Python is the best language.Python is very powerful!PPPPPPPPPP"

print(f"最多的字符是：\'{max(text)[0][0]}\', 共有{max(text)[0][1]}个")