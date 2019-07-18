price = float(input("请输入商品的单价："))
number = int(input("请输入商品的数量："))
money = float(input("请输入支付金额："))
result = money - price * number
print("应该找回"+str(result)+"元钱")