import skill_system.skill_deployer as SkillDeployer

class main:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @staticmethod
    def get_package_name():
        return __name__

# sd = SkillDeployer.SkillDeployer("SkillDeployer")
# print(sd.get_name())
# print(SkillDeployer.SkillDeployer.get_package_name())