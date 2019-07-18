import random
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
    bank = ("建设", "浦发", "华夏", "兴业", "招商", "农业", "民生", "交通", "光大", "平安", "广发", "中信")
    with open("1.txt") as fila01:
        for item in fila01.readlines():
            list_item = item.split(" ")
            print(list_item)
            if list_item[0] in bank:
                dict_credit_card[list_item[0]] = [list_item[1], list_item[2], list_item[3]]
                total_money = float(list_item[3])
                left_money = float(list_item[4])
                min = round(left_money*0.1,0)
                max = round(left_money*0.15,0)
                money = random.randint(min ,max)
                print(money)
                sum += money
            else:
                list_title = [title for title in item]
        print("总共刷了：%d"%sum)


get_info()