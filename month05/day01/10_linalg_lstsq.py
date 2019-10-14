import numpy as np

a = np.arange(1,10).reshape(3,3)
b = np.arange(1,4).reshape(3,1)
print(a)
print(b)

# x = np.linalg.lstsq(a,b)[0]
# print(x)

print(a*b)