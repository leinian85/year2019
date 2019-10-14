import numpy as np

M = np.mat('1 3 7;2 5 7')
print(M)

U,sv,V = np.linalg.svd(M)
print(U * U.T)
print(V * V.T)
print(sv)