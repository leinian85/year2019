# day07 作业
# 1. 三合一
# 2. 当天练习独立完成
# 3. 定义在控制台中打印二维列表的函数
# [
#     [1,2,3,44],
#     [4,5,5,5,65,6,87]
#     [7,5]
# ]
#
# 1 2 3 44
# 4 5 5 5 65 6 87
# 7 5

def print_list(list_target):
    for item in list_target:
        print(" ".join("%d" % i for i in item))


list01 = [
    [1, 2, 3, 44],
    [4, 5, 5, 5, 65, 6, 87],
    [7, 5]
]

print_list(list01)

# 4. (扩展)方阵转置.（不用做成函数）
#     提示：详见图片.
list02 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

list03 = [
    [1, 2, 3, 4],
    [6, 7, 8, 9],
    [11, 12, 13, 14],
    [16, 17, 18, 19]
]


def phalanx_permute(list_phalanx):
    count = 0
    for i in range(len(list_phalanx) - 1):
        for j in range(i + 1, len(list_phalanx)):
            list_phalanx[i][j], list_phalanx[j][i] = list_phalanx[j][i], list_phalanx[i][j]
            count += 1
    print(str(count))
    for item in list_phalanx:
        print(item)


phalanx_permute(list02)
