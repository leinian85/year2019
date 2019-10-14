import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a1 = np.arange(9).reshape((3, 3))
a2 = np.arange(9).reshape((9,))
b = np.clip(a, 3, 6)
b1 = a1.clip(3, 6)
print(b)
print(b1)

c = a2.compress(a2 > 5)
print(c)
print(a2,">>a2")
mask = np.all([a2 > 3, a2 < 7], axis=1)
print(mask)
