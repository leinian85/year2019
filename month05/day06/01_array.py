import numpy as np

a = np.array([-10, 20, 26, 0, 10, -15, 9])
b = np.array([10, 20, 0, 55, -10, -1, 9])
c = np.sign(a)
print(b)
print(c)
print(b * c)

import math as m


def foo(x, y):
    return m.sqrt(x ** 2 + y ** 2)


x, y = np.array([1, 2, 3]), np.array([3, 4, 5])

#矢量化foo函数
foo_vec = np.vectorize(foo) # 返回一个矢量化的函数


print(foo_vec(x, y))
print(np.vectorize(foo)(x,y))