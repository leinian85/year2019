# day11作业
# 1. 三合一
# 2. 当天练习独立完成(使用标准属性封装实例变量exercise03..)
# 3. 请用面向对象思想，描述以下场景：
#     张无忌　教　赵敏　九阳神功
#     赵敏　教　张无忌　化妆
#     张无忌　上班　挣了　10000
#     赵敏　上班　挣了　6000
#     思考：变化点是数据的不同还是行为的不同。


# 4. 请用面向对象思想，描述以下场景：
#     玩家(攻击力)攻击敌人(血量)，敌人受伤(掉血)，还可能死亡(掉装备，加分)。
#     敌人(攻击力)攻击玩家，玩家(血量)受伤(掉血/碎屏),还可能死亡(游戏结束)。
class Enemy:
    def __init__(self,name,ph,atk,defense,empirical_value,money):
        self.name = name
        self.ph = ph
        self.atk = atk
        self.defense = defense
        self.empirical_value = empirical_value
        self.money = money

    @property
    def ph(self):
        return self.__ph

    @ph.setter
    def ph(self,values):
        if values < 0:
            self.__ph = 0
        else:
            self.__ph = values

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self,values):
        self.__atk = values

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self,values):
        self.__defense = values

    @property
    def empirical_value(self):
        return self.__empirical_value

    @empirical_value.setter
    def empirical_value(self,values):
        self.__empirical_value = values

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,values):
        self.__money = values

    def __die(self):
        return(self.empirical_value,self.money)


    def be_attack(self,ph):
        list_bruise = []
        contribution = None
        self.ph -= ph
        if self.ph <= 0:
            if_die = True
            contribution = self.__die()
        else:
            if_die = False
        list_bruise.append(if_die)
        list_bruise.append(self.ph)
        list_bruise.append(contribution)
        return(list_bruise)

    def print_list(self):
        print("%s的血量：%d 攻击力：%d 防御力：%d 经验值：%d 金币：%d"%(self.name,self.ph,self.atk,self.defense,self.empirical_value,self.money))


class Player:
    def __init__(self, name, ph, atk, defense, empirical_value, money):
        self.name = name
        self.ph = ph
        self.atk = atk
        self.defense = defense
        self.empirical_value = empirical_value
        self.money = money

    def attack(self,enemy):
        ph = self.atk - enemy.defense
        list_bruise = enemy.be_attack(ph)
        s_ph = enemy.atk - self.defense
        self.be_attack(s_ph)
        if list_bruise[0]:
            self.empirical_value += list_bruise[2][0]
            self.money += list_bruise[2][1]

    def be_attack(self,ph):
        if self.ph < ph:
            self.ph = 0
            Player.__die()
        else:
            self.ph -= ph

    def print_list(self):
        print("%s的血量：%d 攻击力：%d 防御力：%d 经验值：%d 金币：%d"%(self.name,self.ph,self.atk,self.defense,self.empirical_value,self.money))

    @property
    def ph(self):
        return self.__ph

    @ph.setter
    def ph(self, values):
        if values < 0 :
            self.__ph = 0
        else:
            self.__ph = values

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, values):
        self.__atk = values

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, values):
        self.__defense = values

    @property
    def empirical_value(self):
        return self.__empirical_value

    @empirical_value.setter
    def empirical_value(self, values):
        self.__empirical_value = values

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, values):
        self.__money = values

    @staticmethod
    def __die():
        print("Game Over")

p1 = Player("张无忌",100,80,50,0,0)
e1 = Enemy("小兵",100,110,50,5,100)
for i in range(2):
    p1.attack(e1)
    p1.print_list()
    e1.print_list()
    print("*"*10)