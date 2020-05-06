#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='test_db'
)
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE lleavewords (ids VARCHAR(10),themes VARCHAR(255),peoples VARCHAR(20),times VARCHAR(30))')
# mycursor.execute('ALTER TABLE lleavewords ADD COLUMN ids INT AUTO_INCREMENT PRIMARY KEY')
sql='INSERT INTO lleavewords (ids,themes,peoples,times) VALUES (%s,%s,%s,%s)'
val=[
    ('111','spring','sam','2020-05-01'),
    ('112','summer','tom','2020-05-03'),
    ('113','fall','david','2020-05-02'),
    ('114','winter','coco','2020-05-01'),
    ('115','hope','linda','2020-04-01'),
    ('116','miss','neo','2020-03-21'),
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,'Messaage insert successful!')
sql="DELETE FROM lleavewords WHERE peoples='sam'"    #删除留言人为sam的留言记录
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,'Message delete successful!')
sql="UPDATE lleavewords SET themes ='autumn' WHERE themes ='fall'"  #修改fall主题
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,'Message update successful!')
mycursor.execute('SELECT * FROM lleavewords')
myresult=mycursor.fetchall()
for x in myresult:
    print(x)