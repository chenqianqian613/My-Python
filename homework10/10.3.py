#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
#对2中的表结构，用SQLAchemy模块来实现同样的操作；
# 备注：
#    1 请使用Pycharm开发工具进行开发工作；
#    2 第二题和第三题，用一个虚拟环境；做完了后，生成你的虚拟环境的requirements文件；
from sqlalchemy import Column, Integer, String, Date,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import mysql.connector

#注：create_engine只是创建了一个engine实例，但是它并不会立即去连接数据库，
# 只有在需要连接数据库的操作触发后，engine才会去连接数据库，譬如一个查询操作。
eg = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test_db')
Base = declarative_base()

class testbook(Base):
    __tablename__ = "testbook"
    ID = Column(Integer, primary_key=True)  #设置主键
    leaveword = Column(String(255))
    name = Column(String(255))
    leavetime = Column(Date)
    isdelete = Column(Integer)


def insert():
    s = sessionmaker(eg)
    ds = s()
    ids=input("请输入你的ID：")
    names = input("请输入留言人用户名：")
    word = input("请输入留言：")
    insertword = testbook(ID=ids, leaveword=word, name=names, leavetime=datetime.now(), isdelete=0)
    try:
        ds.add(insertword)
        ds.commit()
        print('留言成功!')
    except Exception as e:
        print(e)
    finally:
        ds.close()

def delete():
    s = sessionmaker(eg)
    ds = s()
    delid=input('请输入要删除的留言的ID：')
    try:
        #ds.query(testbook).filter_by(ID=delid).delete()     这样是真正删掉了该条数据
        result = ds.query(testbook).filter_by(ID=delid).first()   #这样是把isdelete字段置1，没有真正删除该条数据
        result.isdelete = 1
        ds.commit()
        print('删除成功！')
    except Exception as e:
        print(e)
    finally:
        ds.close()

def update():
    s = sessionmaker(eg)
    ds = s()
    upid=input("请输入要更改留言内容的ID：")
    upword=input("请输入更改后的内容：")
    try:
        ds.query(testbook).filter_by(ID=upid).update({"leaveword": upword})
        ds.commit()
        print("留言修改成功！")
    except Exception as e:
        print(e)
    finally:
        ds.close()

def find():
    s = sessionmaker(eg)
    ds = s()
    findid=input("请输入要查找留言的ID：")
    try:
            result = ds.query(testbook).filter_by(ID=findid).one()
            ds.commit()
            if result.isdelete == 1:
                print("所查找的留言已被删除！")
            else:
                print("所查找的留言内容为：ID:{} 姓名：{} 内容：{} 时间：{}".format(result.ID,result.name,result.leaveword,result.leavetime))
    except Exception as e:
        print(e)
    finally:
        ds.close()

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