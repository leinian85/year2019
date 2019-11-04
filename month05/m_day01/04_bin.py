import numpy as np
import sklearn.preprocessing as sp
import scrapy.middleware as sm
import matplotlib.pyplot as mp

a = np.array([
    [10,20,5],
    [2,4,1],
    [10,11,15]
])

bin = sp.Binarizer(threshold=10)
result = bin.transform(a)
print(result)

lily = sm.imread('../素材/da_data/lily.jpg',True)
bin = sp.Binarizer(threshold=127)
result = bin.transform(lily)
mp.imshow(result,cmap='gray')
mp.show()