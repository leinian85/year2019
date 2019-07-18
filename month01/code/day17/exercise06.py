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
    SkillData(104, "黯然销魂掌", 10, 6)
]
l1 = ListHeaper()

count01 = l1.count_self(list_skill,lambda item:len(item.name) > 4)
print(count01)
count02 = l1.count_self(list_skill,lambda item:item.duration <= 5)
print(count02)