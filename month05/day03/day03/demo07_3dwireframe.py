# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo08_3dwireframe.py  三维线框图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
z = (1 - x / 2 + x**5 + y**3) * \
    np.exp(-x**2 - y**2)

# 画图
mp.figure('3D Surface', facecolor='lightgray')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')
ax3d.plot_wireframe(
    x, y, z, cstride=30, rstride=30, linewidth=1,
    color='dodgerblue')
mp.show()
