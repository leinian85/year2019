class DoubleListHelper:

    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name

    @staticmethod
    def get_package_name():
        return __name__
