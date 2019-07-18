"""
    参照day10/exercise02.py
    完成下列练习
"""


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
# 练习1:获取攻击比例大于6的所有技能
# 要求:使用生成器函数/生成器表达式完成

# skills = (Skill for Skill in list_skill if Skill.atk_ratio>6)
# for item in skills:
#     print(item.name)
#
# def findskill():
#     for item in list_skill:
#         if item.atk_ratio>6:
#             yield item
#
# for item in findskill():
#     print(item.name)

re01 = (item for item in list_skill if 4 < item.duration < 11)
for item in re01:
    print(item.name)

re02 = (item for item in list_skill if item.id == 102)
for item in re02:
    print(item.id, item.name)

re03 = (item for item in list_skill if len(item.name) > 4 and item.duration < 6)
for item in re03:
    print(item.id, item.name)
