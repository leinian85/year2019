import matplotlib.pyplot as mp
import numpy as np
from mpl_toolkits.mplot3d import axes3d

n = 300
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
z = np.random.normal(0,1,n)

mp.figure('3D scatter',facecolor='lightgray')
as3d = mp.gca(projection='3d')
as3d.set_xlabel('x')
as3d.set_ylabel('y')
as3d.set_zlabel('z')
d = x**2+y**2+z**2
as3d.scatter(x,y,z,s=70,marker='o',c=d,cmap='jet')
mp.show()