import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0,np.pi*4,1000)
y1 = 4 * np.pi* np.sin(x)

y2 = 4/3*np.pi*np.sin(3*x)
y3 = 4/5*np.pi*np.sin(5*x)
y = y1+y2+y3
mp.grid(linestyle=':')
mp.plot(x,y1,alpha=0.1)
mp.plot(x,y2,alpha=0.2)
mp.plot(x,y3,alpha=0.3)
mp.plot(x,y)
mp.show()