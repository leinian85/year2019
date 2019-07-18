class Enemy:
    def __init__(self,name,stk,ph):
        self.name = name
        self.stk = stk
        self.ph = ph

    @property
    def stk(self):
        return self.__stk

    @stk.setter
    def stk(self,values):
        if values > 0:
            self.__stk = values
        else:
            raise ValueError("NO")

    @property
    def ph(self):
        return self.__ph

    @ph.setter
    def ph(self, values):
        if values > 0:
            self.__ph = values
        else:
            raise ValueError("NO")

en = Enemy("谢逊",50,100)
print(en.stk)
print(en.ph)