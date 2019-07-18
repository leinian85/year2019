'''
day05 作业：
1. 三合一
2. 当前练习独立完成.
3. 计算列表中最小值(不使用min)．
'''
list01 = [12, 10, 5, 14, 2]
minnum = list01[0]
for index in range(1, len(list01)):
    if minnum > list01[index]:
        minnum = list01[index]
print("最小的数是：%d" % minnum)

'''
4. 彩票　双色球：
红球:6个，1 -- 33 之间的整数   不能重复
蓝球:1个，1 -- 16 之间的整数
(1) 随机产生一注彩票[6个红球１个蓝球].

(2) 在控制台中购买一注彩票
提示：
    "请输入第1个红球号码："
    "请输入第2个红球号码："
    "号码不在范围内"
    "号码已经重复"
    "请输入蓝球号码："
'''
import random

list_number = []
count = 0
while True:
    if count < 6:
        number01 = random.randint(1, 33)
        if number01 in list_number:
            # print("号码重复：%d"%number01)
            continue
    else:
        number01 = random.randint(1, 16)
        # print("蓝色球是：%d" % number01)
    list_number.append(number01)
    count += 1
    if count >= 7:
        break

for i in range(0, 5):
    for j in range(0, 5 - i):
        if list_number[j] > list_number[j + 1]:
            list_number[j], list_number[j + 1] = list_number[j + 1], list_number[j]
print("中奖号码：%s" % ("  ".join("%s" % id for id in list_number)))

'''
(2) 在控制台中购买一注彩票
提示：
    "请输入第1个红球号码："
    "请输入第2个红球号码："
    "号码不在范围内"
    "号码已经重复"
    "请输入蓝球号码："
'''
list_number2 = []
if_auto = input("是否机打(机打请输入'Y'):")
if if_auto.upper() == "Y":
    print("老师还没有讲函数，请先手打，谢谢！")

print("******温馨提示：没有钱可以直接按回车键******")
count = 0
while True:
    if count <= 5:
        str_number = input("请输入第%d个红球号码:" % (count + 1))
        if str_number == "":
            break
        number02 = int(str_number)
        if number02 < 1 or number02 > 33:
            print("号码不在范围内")
            continue
        if number02 in list_number2:
            print("号码重复")
            continue
        list_number2.append(number02)
        count += 1
    else:
        str_number = input("请输入蓝球号码:")
        if str_number == "":
            break
        number02 = int(str_number)
        if 1 <= number02 <= 16:
            list_number2.append(number02)
            count += 1
        else:
            print("号码不在范围内")
        if count > 6:
            break

if len(list_number2) == 7:
    for i in range(0, 5):
        for j in range(0, 5 - i):
            if list_number2[j] > list_number2[j + 1]:
                list_number2[j], list_number2[j + 1] = list_number2[j + 1], list_number2[j]
    print("彩票号码：%s" % ("  ".join("%s" % id for id in list_number2)))

    if list_number == list_number2:
        print("恭喜你获得500万大奖，请带上菜刀去银行领取")

'''
5. 阅读python入门到实践第３章和第４章
      程序员的数学第四章

'''
