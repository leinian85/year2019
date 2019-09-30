'''
测试 numpy
'''
import numpy as np

ary = np.array([1, 2, 3, 4, 5, 6])
print(ary)
print(type(ary))
print(ary.shape)  # 维度

ary.shape = (2, 3)  # 维度改为2行3列
print(ary)
print(ary.shape)

ary.shape = (6,)

print(ary)
print(ary * 3)
print(ary > 3)
print(ary + ary)

# ndarray
a = np.array([1, 2, 3])
b = np.arange(0, 10, 2)
print(b)
c = np.zeros(5, dtype="int32")
print(c, c.dtype)

d = np.ones((2, 3), dtype="float32")
print(d, d.shape, d.dtype)

e = d / 5
print(e, e.size)

# 扩展 np.zeros_like()  np.ones_like  维度像...
print(np.zeros_like(a))

print(np.ones_like(b))

# ndarray的属性
a = np.arange(1, 9)
print(a, a.shape)
a.shape = (2, 4)
print(a, a.shape)
print(a.dtype)

# 数据类型的转化 astype()
# a.dtype = "float32"  # 错误的修改数据类型的方式
print(a, a.dtype)

b = a.astype("float32")
print(b, b.dtype)

# 数据的大小 size
print(b, b.size, "lenght:{}".format(len(b)))

# 索引 index
c = np.arange(1, 19)
c.shape = (3, 2, 3)  # 分别代表第一层,第二层,第三层的元素个数
print(c)
print("================")
print(c[1,1,1])

print(c.shape)

for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        for k in range(c.shape[2]):
            print(c[i,j,k])


