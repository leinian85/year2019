import numpy as np

# 基于bool数组的掩码
a = np.arange(1, 100)
# 输出100以内3的倍数
print(a[a % 3 == 0])
# 输出100以内3和7的公倍数
print(a[(a % 3 == 0) & (a % 7 == 0)])

# 基于索引的掩码
names = np.array(["Apple","MI","Mate30 Pro","Oppo","Vivo"])
rank = [1,0,3,4,2]
print(names[rank])
print('-'*80)
rank = [True,False,1,0,1]
print(names[rank])
rank = [True,False,True,True,False]
print(names[rank])