class StackError(Exception):
    pass

class SStack:
    def __init__(self):
        self.list_ = []

    def add(self,val):
        self.list_.append(val)

    def is_empty(self):
        return self.list_ == []

    def pop(self):
        if self.is_empty():
            raise StackError("list is empty")
        return self.list_.pop()

    def top(self):
        if self.is_empty():
            raise StackError("list is empty")
        return self.list_[-1]

    def calcurate(self):
        """
        逆波兰表达式练习
        :return:计算结果
        """
        str_ = input("")
        if str_ == "bc":
            while True:
                str_ = input()
                tmp = str_.split(" ")
                for item in tmp:
                    if item in ("P","p"):
                        print(self.top())
                    elif item in ("+","-","*","/"):
                        num2 = self.pop()
                        num1 = self.pop()
                        str_ = str(num1)+item+str(num2)
                        self.add(eval(str_))
                    else:
                        self.add(item)

s1 = SStack()
s1.calcurate()