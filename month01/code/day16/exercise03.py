class MyRange:
    def __init__(self,num01,num02):
        self.__num01= num01
        self.__num02= num02

    def __iter__(self):
        return MyRange2(self.__num01,self.__num02)

class MyRange2:
    def __init__(self,num01,num02):
        self.__min = num01
        self.__num02 = num02

    def __next__(self):
        if self.__min == self.__num02:
            raise StopIteration
        min = self.__min
        self.__min += 1
        return min


for item in MyRange(1,4):
    print(item)