# 作业:
# 1. 三合一
# 2. 当天练习独立完成
# 3. 定义敌人类(姓名,攻击力,防御力,血量)
#    创建敌人列表,使用list_helper实现下列功能.
#    (1) 查找姓名是"灭霸"的敌人
#    (2) 查找攻击力大于10的所有敌人
#    (3) 查找活的敌人数量
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
#    (1) 查找姓名是"灭霸"的敌人
re1 = l1.find_one(list_enemy,lambda item:item.name == "灭霸")
print(re1.name)

#    (2) 查找攻击力大于10的所有敌人
re2 = l1.find_all(list_enemy,lambda item:item.atk > 10)
for item in re2:
    print(item.name,item.atk)

#    (3) 查找活的敌人数量
re3 = l1.count_self(list_enemy,lambda item:item.ph > 0)
print(re3)

# 5. 阅读：
# 　　　HeadFirst设计模式
# 　　　重构　
#
# 6. 以班级为单位,评选最佳笔记,交给高娜老师.
#    提醒项目经理老师，交面向对象答辩优胜作品.