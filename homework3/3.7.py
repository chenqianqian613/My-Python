#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章),
# 请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
#    比较这2篇文章的相似度
#    (如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);
import re
from collections import Counter


with open('CS1.txt', 'r', encoding='utf-8') as f:
    t1 = f.read()
  # 取出每个单词出现的个数
    c1 = Counter(re.split('\W+', t1))  #split能够按照所能匹配的字串将字符串进行切分，返回切分后的字符串列表
                                  #\W匹配特殊字符，即非字母、非数字、非汉字、非_,\W+还能匹配空格
    r1 = c1.most_common(10)  # 取出频率最高的前10个

with open('CS2.txt', 'r', encoding='utf-8') as f:
    t2 = f.read()
    c2 = Counter(re.split('\W+', t2))
    r2 = c2.most_common(10)

print(r1)
print(r2)
n=6     #输出两篇文章后得到
print("相似度为{:.2f}%".format(n*10))