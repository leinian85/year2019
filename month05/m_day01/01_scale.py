import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17,90,4000],
    [20,80,5000],
    [23,75,5500]
])

result = sp.scale(raw_samples)
print(result)
print(result.mean())
print(result.std())
