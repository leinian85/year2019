'''
输入4位整数
计算每位相加的和
'''
#方法一：
num = int(input("请输入一个4位整数："))
num1 = num % 10
num2 = num % 100 // 10
num3 = num % 1000 // 100
num4 = num // 1000
sum = num1 + num2 + num3 + num4
print("和为：" + str(sum))

#方法二：
result = num % 10
result += num % 100 // 10
result += num % 1000 // 100
result += num // 1000
print("和为：" + str(result))
#分别画出2种方法的内存图
