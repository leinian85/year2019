price = float(input("单价："))
count = int(input("数量:"))
money = float(input("请输入金额："))
result = money - price * count
if result > 0:
    print("应找金额：" + str(result))
elif result == 0:
    print("正好")
else:
    print("钱不够，还差" + str(result * -1))
