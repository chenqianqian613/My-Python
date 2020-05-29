#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）
# （表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#    使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；
import pymysql


def insert():
    db = pymysql.connect("localhost", "root", "password", "test_db")
    cursor = db.cursor()
    ids=input('请输入你的id：')
    name = input("请输入留言人姓名：")
    word = input("请输入留言内容：")
    sql = """insert into testbook (ID,leaveword,name,leavetime,isdelete) VALUES ('"""+ids+"""','"""+word+"""','"""+name+"""',"""+"""CURRENT_TIME ,0)"""

    try:
        cursor.execute(sql)
        db.commit()
        print("留言成功！")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()

def delete():
    db = pymysql.connect("localhost", "root", "password", "test_db")
    cursor = db.cursor()
    deleteid = input("请输入要删除留言的用户ID：")
    sql = """update testbook set isdelete =1 where ID ="""+deleteid   #置为1则为删除
    try:
        cursor.execute(sql)
        db.commit()
        print("成功删除所选择的留言！")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()

def update():
    db = pymysql.connect("localhost", "root", "password", "test_db")
    cursor = db.cursor()
    upid = int(input("请输入要修改留言的ID值："))
    upw = input("请输入修改后的留言内容：")
    sql = """update testbook set leaveword='"""+upw+"""'where ID="""+str(upid)
    try:
        cursor.execute(sql)
        db.commit()
        print("留言修改成功！")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


def find():
    db = pymysql.connect("localhost", "root", "password", "test_db")
    cursor = db.cursor()
    findid = input("请输入要查找留言的ID：")
    sql = "SELECT leaveword, isdelete FROM testbook WHERE id=%s"
    try:
        cursor.execute(sql,(findid,))
        db.commit()
        result = cursor.fetchone()
        if result[1] == 1:  #注意把字段格式设置为整数
            print("所查找的留言已被删除")
        else:
            print("所查找的留言内容为:{}".format(result[0]))

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.close()


if __name__ == '__main__':
    print('欢迎进入留言板！')
    print('1.留言\n2.删除留言\n3.修改留言\n4.查询留言\n0.退出系统！')
    while True:
        n = input('请选择想要进行的功能：')
        if n == '1':
            insert()
        elif n == '2':
            delete()
        elif n == '3':
            update()
        elif n == '4':
            find()
        else:
            break