class Person:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    def get_money(self,bank):
        print(self.name+"在"+bank+"取钱")

class Bank:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

p1 = Person("小明")
b1 = Bank("招商银行")
p1.get_money(b1.name)
