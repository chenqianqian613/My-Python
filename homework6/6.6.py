#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 用面向对象,实现一个学生Python成绩管理系统;
#       学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
#       实现对学生信息及成绩的增,删,改,查方法;
import os


class stupython(object):
    def __init__(self, banji='', num='', name='', pythons=0):
        self.banji = banji
        self.num = num
        self.name = name
        self.pythons = pythons

    def insert(self):
        with open('pythons.txt', 'w',encoding='utf-8')as f:
            f.write('{} {} {} {}\n'.format(self.banji,self.num,self.name,self.pythons))

    def delete(self, key):
            stu = []
            with open('pythons.txt',encoding='utf-8')as f:
                for i in f.readlines():
                    if (i.split(' ')[1] == key):
                        continue
                    else:
                        stu.append(i)
            with open('pythons.txt', 'w',encoding='utf-8')as f:
                for i in stu:
                    f.write(i)

    def exist(self, key):
        with open('pythons.txt',encoding='utf-8')as f:
            for line in f.readlines():
                if (line.split(' ')[1] == key):
                    return True
                else:
                    return False

    def update(self, key):
        if (self.exist(key)):
            self.delete(key)
            self.insert()
        else:
            print('要修改的学生信息不存在！')

    def find(self, key):
        with open('pythons.txt',encoding='utf-8')as f:
            for line in f.readlines():
                s = line.split(' ')
                if (s[1] == key):
                    print('学生信息如下：')
                    print("班级：{} 学号：{} 姓名：{} 成绩：{}".format(s[0], s[1], s[2], s[3]))



if __name__ == '__main__':
    print("——————学生Python成绩管理系统——————")
    while (True): #重复操作
        print('1:增加学生成绩信息')
        print('2:删除学生成绩信息')
        print('3:修改学生成绩信息')
        print('4:查找学生成绩信息')
        print('0：退出系统！')
        choice= int(input("请选择要进行的操作："))
        if (choice == 1):
            banji = input("请输入班级：")
            num = input("请输入学号：")
            name = input("请输入姓名：")
            pythons = input("请输入成绩：")
            s = stupython(banji, num, name, pythons)
            s.insert()
            print("创建学生信息成功！")

        elif (choice == 2):
            s = stupython()
            num = input("请输入要删除信息的学生学号：")
            if (s.exist(num)):
                s.delete(num)
                print("删除成功！")
            else:
                print("要删除的学生信息不存在！请确认后输入")

        elif (choice == 3):
            s = stupython()
            num = input("请输入要修改信息的学生学号：")
            if (s.exist(num)):
                s.delete(num)#先将原信息删除
                banji = input("请输入修改的班级：")
                num = input("请输入修改学号：")
                name = input("请输入修改姓名：")
                pythons = input("请输入修改的成绩：")
                s.__init__(banji, num, name, pythons)
                s.insert()
                print("修改成功!")
            else:
                print("要修改的学生信息不存在！请确认后输入")

        elif (choice == 4):
            s = stupython()
            num = input("请输入要查找的学号：")
            if (s.exist(num)):
                s.find(num)
            else:
                print("要查找的学生信息不存在！")

        else:

            break