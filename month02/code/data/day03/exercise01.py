# 先序:1 2 4 3 5 6 7
# 中序:4 2 1 6 5 7 3
# 后序:4 2 6 7 5 3 1

def fun01(a):
    result = 1
    for i in range(1,a+1):
        result *= i
    return result

print(fun01(5))

def fun02(num):
    if num <= 1:
        return 1
    return num * fun02(num -1)

print("%d!=%d"%(5,fun02(5)))