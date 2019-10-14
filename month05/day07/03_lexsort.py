import numpy as np

names = np.array(['iphone','Huawei','Mi','Vivo','Oppo'])
prices = np.array([5888,2999,2999,2999,2999])
volumes = np.array([60,110,56,89,60])

indices = np.lexsort((volumes,prices))
# 先按价格排序
# 2999 2999 2999 2999 5888
# 110  56   89   60   60
# 1    2    3    4    0
# 在按销量排序
# 2999 2999 2999 2999 5888
# 56   60   89   110  60
# 2    4    3    1    0

print(names[indices])

print('*'*20)

a = np.array([1,9,5,8,6])
b = np.array([7,3])
a = np.msort(a)
print(a)
indices = np.searchsorted(a,b)
print(indices)

c = np.insert(a,indices,b)
print(c)

