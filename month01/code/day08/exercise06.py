'''
排序：[45,89,2,9,46,71]
'''
def rise_list(list01):
    """
    升序排列列表
    :param list01:要排序的列表
    :return:
    """
    for i in range(len(list01)-1):
        for j in range(i+1,len(list01)):
            if list01[i] > list01[j]:
                list01[i],list01[j] = list01[j],list01[i]

list01 = [45,89,2,9,46,71]
rise_list(list01)
print(list01)
str01 = "32165987"
list02 = [int(item) for item in str01]
rise_list(list02)
str02 = "".join("%d"%i for i in list02)
print(str02)