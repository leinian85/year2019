import matplotlib.pyplot as mp
import numpy as np
from mpl_toolkits.mplot3d import axes3d

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))

z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

mp.figure('3D Surface',facecolor='lightgray')
mp.title('contour',fontsize = 18)
ax3d = mp.gca(projection='3d')
ax3d.plot_surface(x,y,z,cstride = 20,rstride= 20,cmap='jet')


mp.show()