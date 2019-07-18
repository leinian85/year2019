import random


class Card:
    def __init__(self, name, bill_date, return_date, total_money, left_money, use_money=0):
        self.name = name
        self.bill_date = bill_date
        self.return_date = return_date
        self.total_money = total_money
        self.left_money = left_money
        self.use_money = use_money

    def set_use_money(self, use_money):
        self.calculate_money()
        self.use_money = use_money

    def calculate_money(self, week=1):
        min = round(self.total_money * 0.1 if week in (6, 7) else self.left_money * 0.1, 0)
        max = round(self.total_money * 0.15 if week in (6, 7) else self.left_money * 0.15, 0)
        self.use_money = random.ranInt(min, max)

    def print_list(self):
        print("%s %s %s %s %s %s ---" % (self.name, self.bill_date, self.return_date, self.total_money, self.left_money,
                                     self.use_money))


'''
{"建设":{
    "账单日":2,
    "还款日":22,
    "总额度":100000,
    "可用额度":100000,
    "刷卡金额":3521.5}
}
'''


def get_info():
    dict_credit_card = {}
    list_title = []
    total_money = 0
    left_money = 0
    sum = 0
    list_card = []
    bank = ("建设", "浦发", "华夏", "兴业", "招商", "农业", "民生", "交通", "光大", "平安", "广发", "中信")
    with open("1.txt") as fila01:
        for item in fila01.readlines():
            list_item = item.replace("\n","").split(" ")
            if list_item[0] in bank:
                card = Card(*list_item)
                list_card.append()
            # list_item = item.split(" ")
            # print(list_item)
            # if list_item[0] in ("建设", "浦发", "华夏", "兴业", "招商", "农业", "民生", "交通", "广大", "平安", "广发", "中信"):
            #     dict_credit_card[list_item[0]] = [list_item[1], list_item[2], list_item[3]]
            #     total_money = float(list_item[3])
            #     left_money = float(list_item[4])
            #     min = round(left_money*0.1,0)
            #     max = round(left_money*0.15,0)
            #     money = random.randint(min ,max)
            #     print(money)
            #     sum += money
            # else:
            #     list_title = [title for title in item]


get_info()
