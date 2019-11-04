import numpy as np

# ndarray 数据类型 一维数组,二维数组,三维数组...多维数组
a = np.array([1,2,3,4,5,6,7,8,9])
print(a,a.dtype,a.shape,a.size)

b = np.arange(1,10).reshape((3,3))
print(b,b.dtype,a.shape,a.size)

c = np.ones(27).reshape((3,3,3))
print(c,c.dtype,c.shape,c.size)

d = np.ones_like(10)
print(d,d.shape)

e = np.zeros(10)
print(e)

f = np.arange(1,28).reshape((3,3,3))
print(f[0:1,0:1,0:1],f[0,0,0],f.size,len(f))
print(f[0:1,0:1,0:1].shape,f[0,0,0].shape)

# 复合数据类型
a = {'name':['a1','a2','a3','a4'],
     'age':[10,11,12,13]}
