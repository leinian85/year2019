class AtkError(Exception):
    def __init__(self,msg,line,atk,id):
        self.msg = msg
        self.line = line
        self.atk = atk
        self.id = id


class Enemy:
    def __init__(self,name,atk):
        self.name = name
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self,values):
        if 0<=values <=100:
            self.__atk = values
        else:
            raise AtkError("攻击力错误",23,"0到100之间","10010")

try:
    e1 = Enemy("外星人",1000)
except AtkError as e:
    print("%s 错误的行数：%d 错误编号：%s 值的范围：%s"%(e.msg,e.line,e.id,e.atk))


