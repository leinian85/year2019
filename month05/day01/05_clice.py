import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9])
a.shape = (3,3)
print(a)
print(a[2:,1:])

b = np.array([1,2,3,4,5,6,7,8,9,10])
c = b.reshape(5,2)
print(c)
print(c[:,0:1])