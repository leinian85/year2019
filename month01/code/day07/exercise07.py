'''
   矩阵转置
'''
list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
'''
[[1, 5, 9, 13], 
 [2, 6, 10, 14], 
 [3, 7, 11, 15], 
 [4, 8, 12, 16]]
'''

list02 = []
for j in range(4):
    list03 = []
    for i in range(len(list01)):
        list03.append(list01[i][j])
    list02.append(list03)
print(list02)

for i in range(4):
    for j in range(i,4):
        if j > i:
            list01[i][j],list01[j][i] = list01[j][i],list01[i][j]
print(list01)