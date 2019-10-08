import matplotlib.pyplot as mp
import numpy as np

mp.figure('pie',facecolor='lightgray')
mp.axis('equal')  # 设置x轴和Y轴等比
values = [23,25,29,28,65]
spaces = [0.05,0.01,0.01,0.01,0.01]
labels = ['php','c','c++','java','python']
colors = ['red','green','orangered','blue','yellow']
mp.pie(values,spaces,labels,colors,'%.1f%%')
mp.legend()
mp.show()