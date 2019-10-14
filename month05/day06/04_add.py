import numpy as np

a = np.arange(1,5)
print(a)
print(np.add(a,a)) # 相加
print(np.add.reduce(a)) # 累加
print(np.add.accumulate(a)) # 递加
print(np.prod(a)) # 累乘
print(np.cumprod(a)) # 递乘

print(np.add.outer([10,20,30],a),">> 外和")
print(np.outer([10,20,30],a),'>>外积')

