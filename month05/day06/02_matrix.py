import numpy as np
ary = np.arange(8).reshape((2,4))
print(ary,type(ary))
m = np.matrix(ary,copy=True)
print(m,type(m))

m2 = np.mat(ary)
print(m2,type(m2))

m3 = np.mat('1 2 3;4 5 6')
print(m3,type(m3))

m = np.mat('1 4 7;2 4 8;3 3 3')
print(m)
print(m.I)
print(m*m.I)

# 解方程
a = np.mat('3 3.2;3.5 3.6')
b = np.mat('118.4;135.2')
print(a.I*b)
print(np.linalg.lstsq(a,b)[0])
print(np.linalg.solve(a,b)) # 解方程

# 输出斐波那契数列
f = np.mat('1 1;1 0')
n = 10
print((f**n)[0,0])