import  common.double_list_helper as DoubleListHelper
class SkillManager:

    def __init__(self, name):
        self.name = name


    def get_name(self):
        return self.name


    @staticmethod
    def get_package_name():
        return __name__

DLH = DoubleListHelper.DoubleListHelper("DoubleListHelper")
print(DLH.get_name())
print(DoubleListHelper.DoubleListHelper.get_package_name())