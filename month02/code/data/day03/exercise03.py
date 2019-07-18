"""
排序
"""

# 冒泡
def bubble_order(list_)
    for i in range(len(list_)-1):
        for j in range(len(list_)-1)
# 插入

# 选择
def select_order(list_):
    for i in range(len(list_)-1):
        for j in range(i+1,len(list_)):
            if list_[i] > list_[j]:
                list_[i],list_[j] = list_[j],list_[i]
        

list01 = [5,4,3,2,1]
bubble_order(list01)
print(list01)