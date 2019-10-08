import matplotlib.pyplot as mp
import numpy as np

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))

z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

mp.figure('contour',facecolor='lightgray')
mp.title('contour',fontsize = 18)
mp.grid(linestyle=":")
cntr = mp.contour(x,y,z,8,colors='black',linewidths=0.5)
mp.clabel(cntr,fmt='%.2f',inline_spacing=2,fontsize = 8)
mp.contourf(x,y,z,8,cmap='jet')
