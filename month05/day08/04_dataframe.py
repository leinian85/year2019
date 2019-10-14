# encoding:utf8
import pandas as pd
import numpy as np

df = pd.DataFrame()
print(df,type(df))

df = pd.DataFrame([1,2,3,4,5])

print(df)
print(df[0])
print(df[0][0])

data = [[40,50],[20,30],[30,55],[70,80]]
data1 = pd.DataFrame(data)
print(data)
data2 = pd.DataFrame(data,index=['张三','李四','王五','赵六'],columns=['语文','数学'])
print(data2)

print(data2[['数学','语文']])

data3 = {"name":['zs','ls','ww'],"age":[10,11,12]}
data4 = pd.DataFrame(data3)
print(data4)
print(data4['age'][1])
print(data4[['age','name']])
print(data4[0:1])

data4['score'] = pd.Series([60,70,68])
print(data4)

del(data4['name'])
print(data4)

data4.pop('age')
print(data4)

print("*"*50)
name = pd.DataFrame([10,11,12])
data3 = {"name":pd.Series(['zs','ls','ww'], index=['a','b','c']),
         "age":pd.Series([10,11,12],index = ['a','b','c'])}
data4 = pd.DataFrame(data3)
print(data4)
print(data4.loc['a'])
print('*'*10)
print(data4.iloc[1,0])

print('*'*10)
data = np.array([['zs',18],['ls',20]])
data2 = pd.DataFrame(data,columns=['name','age'])
dt = pd.DataFrame(np.array([['ww',21]]),columns=['nickname','score'])
print(dt,type(dt))
data2 = data2.append(dt)
print(data2)

print('name','*1'*10)

for data in data2['age']:
    print(data)

print('*2'*10)
data2 = data2.drop(0)
print(data2)

for data in data2['age']:
    print(data)
