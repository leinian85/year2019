
# 方阵转置.（不用做成函数）
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
    """
        将N*N的方阵置换
    :param list_phalanx: 要置换的方阵(列表)
    :return:
    """
    for i in range(len(list_phalanx) - 1):
        for j in range(i + 1, len(list_phalanx)):
            list_phalanx[i][j], list_phalanx[j][i] = list_phalanx[j][i], list_phalanx[i][j]


phalanx_permute(list02)
for item in list02:
    print(item)