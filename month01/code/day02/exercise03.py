a = input("请输入变量1：")
b = input("请输入变量2：")
print("变量1是：" + a)
print("变量2是：" + b)
# c = a
# a = b
# b = c
a, b = b, a
print("交换之后")
print("变量1是：" + a)
print("变量2是：" + b)
