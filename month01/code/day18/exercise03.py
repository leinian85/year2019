from common_test.list_heaper import *
"""
    # 练习１：
    在list_helper.py中增加通用的求和方法.
    案例1:获取敌人列表重所有敌人的名称.
    案例2:获取敌人列表重所有敌人的攻击力.
    案例3:获取敌人列表重所有敌人的名称和血量.
    步骤：
    实现具体功能/提取变化/提取不变/组合
"""
class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "%s--%d--%d--%d" % (self.name, self.hp, self.atk, self.defense)


list01 = [
    Enemy("玄冥二老", 86, 120, 58),
    Enemy("成昆", 0, 100, 5),
    Enemy("谢逊", 120, 130, 60),
    Enemy("灭霸", 0, 1309, 690),
]

l1 = ListHeaper()
print(l1.max_value(list01,lambda item:item.atk))
print(l1.max_value(list01,lambda item:item.defense))
print(l1.max_value(list01,lambda item:item.hp))