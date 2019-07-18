
def estimate_same_unit(list01):
    """
    判断列表中是否存在相同的元素
    :param list01: 列表，字符串，元组
    :return: 返回是否存在相同的元素
    """
    for i in range(len(list01)-1):
        for j in range(i+1,len(list01)):
            if list01[i] == list01[j]:
                return True
    return False
list01 = [1,5,10,2,82,2,10]
result = estimate_same_unit(list01)
print("存在相同的元素" if result else "不存在相同的元素")