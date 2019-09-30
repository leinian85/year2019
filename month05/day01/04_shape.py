import numpy as np

# 视图变维
a = np.arange(1,10)
print(a,a.shape)

b = a.reshape(3,3)
b[0][0] = 10
print(a)
print(b)
a[8] = 90
print(a)
print(b)

print(b.ravel())

# 复制变维
c = a.flatten()
print(c)
c[0] = 1000
print(c)
print(a)

# 就地变维
a.shape = (3,3)
print(a)
a.resize((9,))
print(a)