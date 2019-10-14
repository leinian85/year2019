import pandas as pd
import numpy as np
s = pd.Series()
print(s,type(s),s.dtype)


s1 = np.array([40,50,60,70])
s = pd.Series(s1)
print(s)
print(s[3])
print('切片:',s[-1:])

s = pd.Series(s1,index=['zs','ls','ww','zl'])
print(s)
print(s[3])
print(s['zs'])

s1 = {'zs':10,'ww':30,'ls':20}
s = pd.Series(s1)
print(s,s['zs'],s[2])

for i in s1.values():
    print(i)

#通过标量创建
s = pd.Series(5,index = np.arange(5))
print(s)
s = pd.Series(5)
print(s)

s1 = np.array([0,1,2,4])
s = pd.Series(s1,index=[0,1,2,4])
print(s)
# print(s[3])
