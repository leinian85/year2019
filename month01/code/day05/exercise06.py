list_num = [9,25,12,8]

list_index = []
for item in list_num:
    if item > 10:
        list_index.append(item)

for item in list_index:
    list_num.remove(item)
print(list_num)

list_num = [9,25,12,8]
for i in range(len(list_num)-1,-1,-1):
    if list_num[i] > 10:
        list_num.remove(list_num[i])

print(list_num)
