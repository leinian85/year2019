import copy
class Enemy:
    def __init__(self,name,stk,ph):
        self.name = name
        self.stk = stk
        self.ph = ph

    def __str__(self):
        return "敌人是:%s 攻击力是:%d 血量是:%d"%(self.name,self.stk,self.ph)

    def __repr__(self):
        return "Enemy('%s',%d,%d)"%(self.name,self.stk,self.ph)

e1 = Enemy("外星人",999,1000)

e2 = eval(repr(e1))
e2.name = "地球人"
e3 = copy.deepcopy(e1)
e3.name = "宇宙人"

print(e1)
print(e2)
print(e3)