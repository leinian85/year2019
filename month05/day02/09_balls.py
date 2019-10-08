import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

n = 100
balls = np.zeros(100, dtype=[('position', float, 2),
                             ('size', float, 1),
                             ('growth', float, 1),
                             ('color', float, 4)])

balls['position'] = np.random.uniform(1, 100, (n, 2))
balls['size'] = np.random.uniform(50, 70, n)
balls['growth'] = np.random.uniform(10, 20, n)
balls['color'] = np.random.uniform(0, 1, (n, 4))

mp.xticks([])
mp.yticks([])
sc = mp.scatter(balls['position'][:, 0],
           balls['position'][:, 1],
           s=balls['size'],
           c=balls['color'])


def update(number):
    index = number % 100
    balls['position'][index] = np.random.uniform(0,1,(1,2))
    balls['size'][index] = np.random.uniform(50,70,1)
    balls['size'] += balls['growth']
    # 重新绘制
    sc.set_offsets(balls['position'])
    sc.set_sizes(balls['size'])

anim = ma.FuncAnimation(mp.gcf(),update,interval=30)

mp.show()
