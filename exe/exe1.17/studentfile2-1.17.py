#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 练习4
# :   一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出到另外一个文件中:
#             姓名      学号      分数
#             张三      101         78
#             李四      102         87
#             王五       103        83

# f=open(r'C:\Users\windows\Desktop\yyy\new 1', 'r', encoding='utf-8')   #打开原文件（要读的文件）
# f2=open(r'C:\Users\windows\Desktop\yyy\studnet.txt', 'w', encoding='utf-8') #打开要写入的文件
# l=[]
# sort=[]
# for line in f:  # 遍历每一行
#         wordlist = line.split()  # 将每一行的数字分开放在列表中
#         l.append(wordlist[2])
#         sort=sorted(l)
# f2.write(sort[0]+"\n")
# f2.write(sort[1]+"\n")
# f2.write(sort[2]+"\n")
# f.close()
# f2.close()


# #练习5：一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出;
#             姓名      学号      分数
#             张三      101         78
#             李四      102         87
#             王五       103        83
f=open(r'C:\Users\windows\Desktop\yyy\new 1', 'r', encoding='utf-8')
l=[]
sort=[]
for line in f:  # 遍历每一行
         wordlist = line.split()  # 将每一行的数字分开放在列表中
         l.append(wordlist[2])
         sort=sorted(l)
print(sort[0])
print(sort[1])
print(sort[2])
f.close()







