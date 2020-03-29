#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#对一篇英文文章，进行词频统计，输出前10个出现频率最高的单词；
# 提示：
#  1 可以先定义一个函数，专门来处理英文文章的读取问题；
#  读取时，解决大小写问题，以及标点符号问题（如，将标点符号都替换成空格）；

from collections import Counter
import re
def getText():
    txt=open('article.txt', 'r',encoding='utf-8').read()
    txt=txt.lower()     # lower() 方法转换字符串中所有大写字符为小写。
    for ch in '!"#$&()*+,-./:;<>=?@[]\\^_{}|~':
        txt=txt.replace(ch," ")
    return txt
txt=getText()
# 取出每个单词出现的个数
t1 = Counter(re.split(r' ', txt))  #split能够按照所能匹配的字串将字符串进行切分，返回切分后的字符串列表
                                  #也可以用re.split('\W',txt)匹配特殊字符，即非字母、非数字、非汉字、非_,直接取出特殊字符
ttt = t1.most_common(11)  # 取出频率最高的前10个,第一位一般是空格，所以取前十一位
print(ttt)