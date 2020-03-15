#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
#  提示：可以用字典来统计：key 是单词，value 是单词出现次数；
#  先创建一个字典，然后遍历刚刚取出的单词列表，
#  接着做一个判断： 如果字典中 key 已经出现了这个单词，那么它对应的 value ，也就是出现次数就 +1；
#  如果这个单词没出现过，就直接 插入这个单词及 value 为 1 到 字典中；
text = "To see a world in a grain of sand, and a heaven in a wild fllower, hold infinity in the palm of your hand, and eternity in an hour. "
list = text.split()
num = {}
for i in range(len(list)):
    if list[i] in num.keys():
        num[list[i]] += 1
    else:
        num[list[i]] = 1
sortedfrdict = sorted(num.items(), key = lambda x : x[1], reverse = True )

for i in range(len(sortedfrdict)):
    print(f"{sortedfrdict[i][0]}: {sortedfrdict[i][1]}")

