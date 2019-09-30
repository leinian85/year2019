import numpy as np
import matplotlib.pyplot as mp

x = np.array([1,2,3,4,5,6])
y = np.array([7,8,9,10,11,12])
mp.vlines(1,7,12)
mp.hlines(7,1,6)

mp.plot(x,y)
mp.show()
