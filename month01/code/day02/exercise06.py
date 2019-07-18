'''
古代的秤是1斤为16两
输入两，计算是几斤几两
'''
num = int(input("请输入两："))
num1 = num // 16
num2 = num % 16
if num1 == 0:
    print("显示为" + str(num2) + "两")
elif num2 == 0:
    print("显示为" + str(num1) + "斤")
else:
    print("显示为" + str(num1) + "斤" + str(num2) + "两")

'''
在控制台输入距离，时间，初速度，计算加速度
加速度 = （距离 - 初速度 × 时间）×2/时间平方
'''
length = int(input("距离为："))
time = int(input("时间为："))
speed_start = float(input("初速度为："))
speed_add = (length - speed_start * time) * 2 / time ** 2
print("加速度为：" + str(speed_add))
