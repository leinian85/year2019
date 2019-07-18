list01 = [57, 40, 12, 45, 30, 11, 2]
list02 = []
for item in list01:
    if item > 30:
           list02.append(item)
print(list02)

list01 = [57, 40, [10,5]]
list02 = []
for item in list01:
    list02.append(item)
list01[2][0] = 0
print(list02[2][0])

# list_num = []
# for i in range(0,5):
#     temp_num = int(input("请输入数字："))
#     list_num.append(temp_num)

# for i in range(0,4):
#     if list_num[i] > list_num[i+1]:
#         list_num[i],list_num[i+1] = list_num[i+1],list_num[i]
#
# print(list_num[-1])
list_num = [5, 6, 7, 8, 9]
count=0
for j in range(4):
    for i in range(0,4):
        count += 1
        if list_num[i] > list_num[i+1]:
            list_num[i],list_num[i+1] = list_num[i+1],list_num[i]

print(list_num)
print(count)

list_num = [5, 6, 7, 8, 9]
count=0
for j in range(4,-1,-1):
    for i in range(0,j):
        count += 1
        if list_num[i] > list_num[i+1]:
            list_num[i],list_num[i+1] = list_num[i+1],list_num[i]
print(list_num)
print(count)