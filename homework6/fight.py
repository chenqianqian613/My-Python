#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 请写一个小游戏，人狗大站;  规则:
#     1、
#     2个角色，人和狗，游戏开始后，生成2个人，3条狗，
#     人狗互相交替对战(注意,人只能打狗,狗也只会咬人);
#     人的打击力为10;  初始化血为100;
#     狗的攻击力为 15; 初始化血为80;
#     2、
#     人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。
#     血为0的话,表示死亡,退出游戏;
#     人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
#     3、
#     对战规则:
#      A  随机决定,谁先开始攻击;
#      B  一方攻击完毕后, 另外一方再开始攻击;
#         攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
#      C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
#提示：注意组织代码的方式；狗类用一个单独的py文件； 人用一个单独的py文件；
# 在写一个fight模块（也用类来组织；在这个模块中，导入人和狗模块中编写好的方法）

import random
from dog import ddd
from people import ppp

def display(dogs,people):
    print('#当前场上人狗选手剩余情况#')
    for i in range(len(dogs)):
        print('{}号狗选手的剩余血量：{}，攻击力：{}'.format(dogs[i].num,dogs[i].blood,dogs[i].strong))
    print('~~'*20)
    for j in range(len(people)):
        print('{}号人选手的剩余血量：{}，打击力：{}'.format(people[j].num,people[j].blood,people[j].strong))




if __name__=='__main__':
    print("--"*30)
    print("人狗大战开始!")

    d1=ddd()
    d2=ddd()
    d3=ddd()
    dogs=[d1,d2,d3]

    p1=ppp()
    p2=ppp()
    people=[p1,p2]
    display(dogs,people)
    first=random.choice([0,1])   #随机决定攻击的顺序，1代表人先攻击
    round=1
    while(len(dogs)>0 and len(people)>0):#在人和狗数量都不为0时才能继续游戏

        print("--"*30)
        print('第{}回合'.format(round))
        if(first==0):
            print("此回合由狗攻击人")
            d = random.randint(0, len(dogs) - 1)#随机选择狗和人选手
            firstdog=dogs[d]
            p=random.randint(0,len(people)-1)
            firstpeople=people[p]
            firstpeople.attack(firstdog)
            if(firstpeople.blood<=0):
                print('一位人选手血量耗尽，阵亡！')
                people.pop(p)  #pop方法，删除一个人选手

            first=1
        else:
            print("此回合由人攻击狗")
            pp = random.randint(0, len(people) - 1)
            firstpeople=people[pp]
            dd=random.randint(0,len(dogs)-1)
            firstdog=dogs[dd]
            firstdog.attack(firstpeople)
            if(firstdog.blood<=0):
                print('一位狗选手血量耗尽，阵亡！')
                dogs.pop(dd)
            first=0
        display(dogs,people)
        round+=1

    if(len(people)<=0):
        print("人狗大战比赛最终狗获胜！")
    else:
        print("人狗大战比赛最终人获胜！")
