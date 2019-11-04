import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17,90,4000],
    [20,80,5000],
    [23,75,5500]
])

# mms = sp.MinMaxScaler(feature_range=(0,1))
# result = mms.fit_transform(raw_samples)
# print(result)

for row in raw_samples.T:
    min_val = row.min()
    max_val = row.max()

    A = np.array([[min_val,1],[max_val,1]])
    B = np.array([0,1])
    print(A)
