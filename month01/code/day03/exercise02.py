'''
在控制台输入季度，显示相应的月份
'''
quarter = input("请输入一个季度：")
if quarter == "春":
    print("1月2月3月")
elif quarter == "夏":
    print("4月5月6月")
elif quarter == "秋":
    print("7月8月9月")
elif quarter == "东":
    print("10月11月12月")
else:
    print("输入错误")


num1 = float(input("输入第一个数字："))
sign = input("输入一个符号：")
num2 = float(input("输入第二个数字："))
if sign not in ("+", "-", "*", "/"):
    print("运算符有误")
else:
    if sign == "+":
        result = num1 + num2
    elif sign == "-":
        result = num1 - num2
    elif sign == "*":
        result = num1 * num2
    elif sign == "/":
        result = num1 / num2
    print(str(num1) + sign + str(num2) + "=" + str(result))

num1 = int(input("请输入数字1："))
num2 = int(input("请输入数字2："))
num3 = int(input("请输入数字3："))
num4 = int(input("请输入数字4："))
if num1 > num2:
    temp = num1
else:
    temp = num2
if temp < num3:
    temp = num3
if temp < num4:
    temp = num4
print("最大的数是：" + str(temp))
