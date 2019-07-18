# 4. 在list_helper中增加判断是否存在某个对象的方法.返回值:true/false
#    案例1:判断敌人列表中是否存在"成昆"
#    案例2:判断敌人列表中是否攻击力小于5或者防御力小于10的敌人.
#     步骤:
#     实现每个需求/单独封装变化/定义不变的函数("继承"/"多态")
#     将不变的函数提取到list_helper.py中
#     体会：函数式编程的思想("封装，继承，多态")

from common.list_heaper import *

class Enemy:
    def __init__(self,name,atk,ph):
        self.name = name
        self.atk = atk
        self.ph = ph

list_enemy = [
    Enemy("灭霸",5,100),
    Enemy("灭绝师太",5,95),
    Enemy("成昆",7,90),
    Enemy("裘千仞",13,91),
    Enemy("玄冥二老",6,105),
    Enemy("颜良",17,0)
]

l1 = ListHeaper()
#    案例1:判断敌人列表中是否存在"成昆"
e1 = l1.if_exist(list_enemy,lambda item:item.name == "成昆1")
print(e1)

#    案例2:判断敌人列表中是否攻击力小于5或者防御力小于10的敌人.
e2 = l1.if_exist(list_enemy,lambda item:item.atk <5 or item.ph > 100)
print(e2)

print(r"dqad\nwq")