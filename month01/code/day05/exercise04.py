list01= [800,1000]
list02 = list01[:]
list01[0] = 900
print(list02[0])

# list01 = [800,[1000,500]]
# list02 = list01
# list01[1][0] = 900
# print(list02[1][0])
list01 = [800,[1000,500]]
list02 = list01[:]
list01[1][0] = 900
print(list02[1][0])