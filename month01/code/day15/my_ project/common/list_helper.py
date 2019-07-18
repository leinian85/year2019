import main
class ListHelper:


    def __init__(self, name):
        self.name = name


    def get_name(self):
        return self.name


    @staticmethod
    def get_package_name():
        return __name__

m = main.main("Main")
print(m.get_name())
print(main.main.get_package_name())
