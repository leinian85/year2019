from common_test.list_heaper import *


# 作业
# 1.三合一（闭包）
# 2.当天练习独立完成(list_helper.py)
# 3.在list_helper.py中新增以下功能：
#     (1)获取最小值
#     (2)降序排列
#     (3)根据指定条件删除元素
#        案例:在敌人列表中，删除所有死人.
#        案例:在敌人列表中，攻击力小于50的所有敌人.
#        案例:在敌人列表中，防御力大于100的所有敌人.
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
    Enemy("谢逊", 120, 30, 60),
    Enemy("灭霸", 0, 1309, 690)
]

#     (1)获取最小值
l1 = ListHeaper()
print(l1.min_value(list01, lambda item: item.atk))

#     (2)降序排列
l1.fall(list01, lambda item: item.atk)
for item in list01:
    print(item)
#     (3)根据指定条件删除元素
#        案例:在敌人列表中，删除所有死人.
#        案例:在敌人列表中，攻击力小于50的所有敌人.
#        案例:在敌人列表中，防御力大于100的所有敌人.
print("-----------------")
l1.my_remove(list01, lambda item: item.hp == 0)
for item in list01:
    print(item)

print("-----------------")
l1.my_remove(list01, lambda item: item.atk <= 50)
for item in list01:
    print(item)

print("-----------------")
l1.my_remove(list01, lambda item: item.defense >= 100)
for item in list01:
    print(item)

# 4. 阅读"面向对象答辩优胜者"文档.
#    总结出属于自己的话术，以便就业准备简历时使用(介绍项目).
