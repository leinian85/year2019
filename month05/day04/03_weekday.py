import numpy as np
ary = np.arange(1,37).reshape(6,6)
def apply(data):
    return data.mean()

print(ary)

r = np.apply_along_axis(apply,1,ary)
print(r)

print(apply(ary[0,:]))