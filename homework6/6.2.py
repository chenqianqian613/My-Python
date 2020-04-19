#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#定义一个学生Student类。有下面的类属性：
# 1 姓名 name
# 2 年龄 age
# 3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下:
class student():
    name = ''
    age = 0
    score = {'语文': 0,'数学': 0,'英语': 0}
    def __init__(self,name,age,ch,ma,en):
        self.name=name
        self.age=age
        self.score['语文'] = ch
        self.score['数学'] = ma
        self.score['英语'] = en
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.score)
s1=student('陈明',18,98,87,88)
s2=student('王娟',17,87,90,76)
print('学生一信息如下')
print('姓名为：',s1.get_name())
print('年龄为:',s1.get_age())
print('最高分为：',s1.get_course())
print('\n')
print('学生二信息如下')
print('姓名为：',s2.get_name())
print('年龄为',s2.get_age())
print('最高分为：',s2.get_course())