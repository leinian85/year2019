import matplotlib.pyplot as mp
import numpy as np

apples = np.array([50, 42, 96, 35, 25, 162, 14, 155, 14, 123, 32, 65])
oranges = np.array([99, 77, 88, 36, 56, 48, 95, 62, 61, 32, 25, 44])
mp.figure('Bar', facecolor='lightgray')
mp.title('Bar', fontsize=18)
mp.grid(linestyle=':')
x = np.arange(apples.size)
mp.bar(x - 0.2, apples, 0.4, color='limegreen', label='apples')
mp.bar(x + 0.2, oranges, 0.4, color='red', label='oranges')

mp.xticks(x,['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
mp.legend()
mp.show()
