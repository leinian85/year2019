import numpy as np
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)

print(np.zeros(10))
print(np.zeros((3, 6)))
print(np.empty((2, 3, 2)))

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)
empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)

arr = np.random.randn(5, 4)
print(arr)
print(arr.mean())
print(np.mean(arr))
print(arr.sum())
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr)
print(arr.cumsum(axis=0))
print(arr.cumprod(axis=1))

#unique
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))
#dot
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(x.dot(y))
print(np.dot(x, y))
#normal
samples = np.random.normal(size=(4, 4))
print(samples)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[:2,1:],arr[:2,1:].shape)
print(arr[2],arr[2].shape)
print(arr[2,:],arr[2,:].shape)
print(arr[2:,:],arr[2:,:].shape)
print(arr[:,:2],arr[:,:2].shape)
print(arr[1,:2],arr[1,:2].shape)
print(arr[1:2,:2],arr[1:2,:2].shape)