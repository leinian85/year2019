[TOC]
### 列表推导式
```
list01 = [1,2,3]
list02 = []
for item in list01():
    list02.append(item)
```
```
#等同于：
list02 = [item for item in list01]
```
### 求列表中的最小值
![](../day06/求最小值内存图.jpg)