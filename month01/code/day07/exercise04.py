'''
排序：[45,89,2,9,46,71]
'''
list01 = [45,89,2,9,46,71]
# for i in range(5):
#     for j in range(5-i):
#         if list01[j] > list01[j+1]:
#             list01[j],list01[j+1] = list01[j+1],list01[j]
# print(list01)

for i in range(len(list01)-1):
    for j in range(i+1,len(list01)):
        if list01[i] > list01[j]:
            list01[i],list01[j] = list01[j],list01[i]
print(list01)