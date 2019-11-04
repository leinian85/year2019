import numpy as np
import sklearn.preprocessing as sp

s = np.array([
    [1,5,9],
    [2,5,6],
    [1,3,7],
    [1,5,0]
])

ohe = sp.OneHotEncoder(sparse=False,dtype='int32')
result = ohe.fit_transform(s)
print(result)