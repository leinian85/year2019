import numpy as np

a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)

# 水平方向
c = np.hstack((a,b))
print(c)

d,e,f = np.hsplit(c,3)
print(d)
print(e)
print(f)

# 垂直方向
c = np.vstack((a,b))
print(c)
d,e = np.vsplit(c,2)
print(d)
print(e)

# 深度方向
print('*'*30)
c = np.dstack((a,b))
print(c)
d,e = np.dsplit(c,2)
print(d)
print(e)

# 一位数组的组合
a = np.arange(1,9)
b = np.arange(9,17)
print(a)
print(b)
print(np.row_stack((a,b)))  # 形成2行
print(np.column_stack((a,b))) # 形成2列