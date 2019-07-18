"""
    property 的演变：exercise01,exercise02,exercise03
"""
class Enemy:
    def __init__(self,name,stk,ph):
        self.name = name
        self.set_stk(stk)
        self.set_ph(ph)

    def set_stk(self,values):
        if values > 0:
            self.__stk = values
        else:
            raise ValueError("NO")

    def get_stk(self):
        return self.__stk

    def set_ph(self,values):
        if values > 0 :
            self.__ph = values
        else:
            raise ValueError("NO")

    def get_ph(self):
        return self.__ph

en = Enemy("谢逊",50,100)
print(en.get_stk())
print(en.get_ph())