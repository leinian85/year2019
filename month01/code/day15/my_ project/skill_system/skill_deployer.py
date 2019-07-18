import skill_system.skill_manager as SkillManager
class SkillDeployer:

    def __init__(self, name):
        self.name = name


    def get_name(self):
        return self.name


    @staticmethod
    def get_package_name():
        return __name__

sm = SkillManager.SkillManager("SkillManager")
print(sm.get_name())
print(SkillManager.SkillManager.get_package_name())