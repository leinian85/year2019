list01 = [1,"as",120.5,0,"nasui",3,10,"da",80]

class finsstr():
    def __init__(self,iterable_taget,type):
        self.__list01 = iterable_taget
        self.__type = type

    def get_item01(self):
        for item in self.__list01:
            if type(item) == type(self.__type):
                yield item

    def get_item02(self):
        return (item for item in list01 if type(item) == type(self.__type))

    def get_item03(self):
        return [item for item in list01 if type(item) == type(self.__type)]


re1 = finsstr(list01,"0")
for item in re1.get_item01():
    print(item)

for item in re1.get_item02():
    print(item)

re2 = re1.get_item03()
print(re2)

re3 = finsstr(list01,0.0)
for item in re3.get_item01():
    print(item)

for item in re3.get_item02():
    print(item)

re4 = re3.get_item03()
print(re4)

