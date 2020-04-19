#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
# #       封装方法，求单个学生的总分，平均分，以及打印学生的信息。
class student():

  def __init__(self, name, age, sex, English, math, Chinese):
    self.name = name
    self.age = age
    self.sex = sex
    self.English = English
    self.math = math
    self.Chinese = Chinese
  def getsum(self):
      return self.English+self.math+self.Chinese
  def getaverage(self):
      return ((self.English+self.math+self.Chinese)/3)
  def prin(self):
      print('学生信息如下：')
      print('姓名为：',self.name)
      print('年龄为: ',self.age)
      print('性别为：',self.sex)
      print('英语成绩为：',self.English)
      print('数学成绩为：',self.math)
      print('语文成绩为：',self.Chinese)
      print('该学生总分为: ',self.getsum())
      print('该学生平均分为：',self.getaverage())
      print('\n')

s1=student('Alice',18,'女',100,76,89)
s1.prin()
s2=student('Sam',19,'男',78,89,90)
s2.prin()

