from common_test.list_heaper import *

class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
]

def condition01(item):
    return item.name == "葵花宝典"

def condition02(item):
    return item.id == 101

def condition03(item):
    return item.duration > 0

l1 = ListHeaper()
item01 = l1.find_one(list_skill,condition01)
print(item01.name)

item02 = l1.find_one(list_skill,condition02)
print(item02.id)

item03 = l1.find_all(list_skill,condition03)
for item in item03:
    print(item.duration)