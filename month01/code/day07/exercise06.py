list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

print("打印第二行第三个元素:")
print(list01[1][2])
print("打印第三行每个元素:")
for i in range(len(list01[2])):
    print(list01[2][i])
print("打印第一列每个元素:")
for i in range(len(list01)):
    print(list01[i][0])