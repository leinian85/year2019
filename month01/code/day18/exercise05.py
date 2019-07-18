from common.list_helper import *
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
    Enemy("魔童", 86, 120, 58),
    Enemy("成昆", 0, 100, 5),
    Enemy("谢逊", 120, 130, 60),
    Enemy("灭霸", 0, 1309, 690),
]

t1 = ([1,1,1],[2,2],[3,3,3,3])

#1 获取最大长度的列表
l1 = ListHelper()
max_value = l1.get_max(t1,lambda item:len(item))
print(max_value)
#2 根据敌人列表,获取所有敌人的姓名与血量与攻击力
# for item in l1.find_all(list01,lambda item:item):
#     print(item)
for item in map(lambda item:(item.name,item.hp,item.atk),list01):
    print(item)

#3 在敌人列表中,获取攻击力大于100的所有活人
for item in l1.find_all(list01,lambda item:item.atk>100 and item.hp > 0):
    print(item)

#4 根据防御力对敌人列表进行降序排列
list02 = sorted(list01,key = lambda item:item.defense,reverse=True)
for item in list02:
    print(item)
