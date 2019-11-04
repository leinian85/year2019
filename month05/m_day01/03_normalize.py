import numpy as np
import sklearn.preprocessing as sp

a = np.array([
    [10,20,5],
    [2,4,1],
    [10,11,15]
])

result = sp.normalize(a,norm='l1')
print(result)