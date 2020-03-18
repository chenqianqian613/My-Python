#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#构造上述文件结构,分别在指定位置打开文件进行写入操作;
# 同级文件夹里面打开;  同级目录下的子目录里面打开; 上一级文件目录中的其他文件夹中打开
#需要自己在桌面创建两个文件夹ppp和yyy，ppp中有121.txt和122.txt，yyy中有123.txt
f = open(r'C:\Users\windows\Desktop\ppp\121.txt', 'w+', encoding='gbk')
f.write('今天是 ')
with open(r"C:\Users\windows\Desktop\ppp\122.txt","w+") as file:
    file.write('天气很好')
with open(r"C:\Users\windows\Desktop\yyy\123.txt", "w+") as f2:
    f2.write('美好的一天')
f.close()
f2.close()
file.close()