# 列表推导式
list01 = [i ** 2 for i in range(1, 11)]
list02 = [item for item in list01 if item % 2 == 1]
list03 = [item for item in list01 if item % 2 == 0]
list04 = [item + 1 for item in list01 if item % 2 == 0 and item > 5]
list05 = [item + 1 for item in list03 if item > 5]
print(list01)
print(list02)
print(list03)
print(list04)
print(list05)
