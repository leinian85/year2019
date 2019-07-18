"""
函数参数
"""


# 缺省（默认）参数：如果实参不传入，可以使用默认值
def fun01(a, b="a", c=3, d=0):
    print(a)
    print(b)
    print(c)
    print(d)


# 1.关键字实参 + 缺省形参：调用者可以随意传递参数
fun01(a=1, b=2)


# 2.位置参数
def fun02(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


# 3.星号元组形参：星号将所有实参合并为一个元组
def fun03(*args):
    print(args)

fun03(1, 2, "a")
#4.命名关键字形参：
def fun04(a,*args,b):
    print(a)
    print(args)
    print(b)

fun04("a",b="a")

#5.双星号字典形参
def fun06(**a):
    print(a)

fun06(a=1,b=2)