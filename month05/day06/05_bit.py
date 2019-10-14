import numpy as np

a = np.array([-9,-5,21,9,-2])
b = np.array([-2,6,-2,3,-9])

c = a^b
print(a^b)
print(np.bitwise_xor(a,b))
print(np.where(c<0))