"""
    技能系统
"""


class SkillImpactEffect:
    """
        技能影响效果
    """

    def impact(self):
        raise NotImplementedError()


class DamageEffect(SkillImpactEffect):
    """
        伤害生命效果
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print("扣你%d血" % self.value)


class LowerDeffenseEffect(SkillImpactEffect):
    """
        降低防御力
    """

    def __init__(self, value, time):
        self.value = value
        self.time = time

    def impact(self):
        print("降低%d防御力,持续%d秒" % (self.value, self.time))


class DizzinessEffect(SkillImpactEffect):
    """
        眩晕
    """

    def __init__(self, time):
        self.time = time

    def impact(self):
        print("眩晕%d秒" % self.time)


class SkillDeployer:
    """
        技能释放器
    """

    def __init__(self, name):
        self.name = name
        # 加载配置文件 {技能名称:[效果1,效果2...],...}
        self.__dict_skill_config = self.__load_config_file()
        # 创建效果对象
        self.__effect_objects = self.__create_effect_objects()

    def __load_config_file(self):
        # 加载文件.....
        return {
            "降龙十八掌": ["DamageEffect(200)", "LowerDeffenseEffect(-10,5)", "DizzinessEffect(6)"],
            "六脉神剑": ["DamageEffect(100)", "DizzinessEffect(6)"]
        }

    def __create_effect_objects(self):
        # 根据name创建相应的技能对象
        #    降龙十八掌 -> ["技能1"，"技能2"]
        list_effect_name = self.__dict_skill_config[self.name]
        list_effect_object = []
        for item in list_effect_name:
            # "技能1" --> 技能1的对象
            # 对象 = eval("DamageEffect(200)")
            effect_object = eval(item)
            list_effect_object.append(effect_object)
        return list_effect_object

    # 生成技能(执行效果)
    def generate_skill(self):
        print(self.name, "技能释放啦")
        for item in self.__effect_objects:
            # 调用父类，执行子类.
            item.impact()


xlsbz = SkillDeployer("降龙十八掌")
xlsbz.generate_skill()

lmsj = SkillDeployer("六脉神剑")
lmsj.generate_skill()
