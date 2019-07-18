# 4. 定义敌人类
#     --　数据:姓名,血量,基础攻击力,防御力
#     --　行为:打印个人信息
#
#    创建敌人列表(至少４个元素),并画出内存图。
#    查找姓名是"灭霸"的敌人对象
#    查找所有死亡的敌人
#    计算所有敌人的平均攻击力
#    删除防御力小于10的敌人
#    将所有敌人攻击力增加50

class Enemy:
    """
    敌人类
    """
    count = 0

    def __init__(self, name, anima, attack_size, recovery_size):
        self.name = name
        self.anima = anima
        self.attack_size = attack_size
        self.recovery_size = recovery_size
        Enemy.count += 1

    def print_self_info(self):
        print("%s:生命值：%d 攻击力：%d 防御力：%d" % (self.name, self.anima, self.attack_size, self.recovery_size))

    @staticmethod
    def get_info_for_name(name, list_enemy):
        for enemy in list_enemy:
            if enemy.name == name:
                return enemy

    @staticmethod
    def get_enemy_of_die(list_enemy):
        list_die_enemy = []
        for enemy in list_enemy:
            if enemy.anima == 0:
                list_die_enemy.append(enemy)
        return list_die_enemy

    @staticmethod
    def get_average_attack(list_enemy):
        list_attack = []
        for enemy in list_enemy:
            list_attack.append(enemy.attack_size)
        return sum(list_attack)/len(list_attack)

    @staticmethod
    def del_enemy_for_attack(attack,list_enemy):
        for enemy in list_enemy:
            if enemy.attack_size < attack:
                list_enemy.remove(enemy)

    @staticmethod
    def add_attact(attact,list_enemy):
        for enemy in list_enemy:
            enemy.attack_size += attact

    @staticmethod
    def print_all_enemy(list_enemy):
        for enemy in list_enemy:
            enemy.print_self_info()



list_enemy = [
    Enemy("曹操", 9999, 1000, 500),
    Enemy("孙权", 0, 900, 800),
    Enemy("刘备", 5000, 1300, 200),
    Enemy("董卓", 0, 888, 888)
]

enemy = Enemy.get_info_for_name("曹操",list_enemy)
if enemy:
    enemy.print_self_info()

list_die_enemy = Enemy.get_enemy_of_die(list_enemy)
for enemy in list_die_enemy:
    enemy.print_self_info()
print("平均攻击力：%d"%Enemy.get_average_attack(list_enemy))

Enemy.del_enemy_for_attack(900,list_enemy);
Enemy.print_all_enemy(list_enemy)

Enemy.add_attact(50,list_enemy)
Enemy.print_all_enemy(list_enemy)
